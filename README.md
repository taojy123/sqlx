# sqlx

SQL Extension

一种扩展 sql 的语言，目标是打造 "易读易写 方便维护" 的 sql 脚本


## 语法简介

### 1. 通过 `define` 定义变量，可在脚本中反复引用

示例:
```sql
define field_name age

SELECT {field_name} from students WHERE {field_name} > 10;
SELECT {field_name} from teachers WHERE {field_name} > 10;
```

编译生成 sql 为:
```sql
SELECT age from students WHERE age > 10;
SELECT age from teachers WHERE age > 10;
```


### 2. 通过 `block` 定义脚本片段，并反复引用

示例:
```sql
-- ! 定义片段
block good_students(score)
    (
        SELECT
            *
        FROM
            students
        WHERE
            score > {score}
    ) AS good_students
endblock

SELECT name FROM {good_students(80)};
SELECT count(*) FROM {good_students(80)};
```

编译生成 sql 为:
```sql
SELECT name FROM 
    (
        SELECT
            *
        FROM
            students
        WHERE
            score > 80
    ) AS good_students
;
SELECT count(*) FROM 
    (
        SELECT
            *
        FROM
            students
        WHERE
            score > 80
    ) AS good_students
;
```


### 3. 循环
通过 `for` 批量循环生成脚本（暂不支持循环嵌套）



示例1:
```sql
{% for n in table1,table2,table3 %}
    SELECT * FROM {n};
{% endfor %}
```

编译生成 sql 为:
```sql
SELECT * FROM table1;
SELECT * FROM table2;
SELECT * FROM table3;
```


示例2:
```sql
{% for n|m in table1|id,table2|name,table3|age %}
    SELECT {m} FROM {n};
{% endfor %}
```

编译生成 sql 为:
```sql
SELECT id FROM table1;
SELECT name FROM table2;
SELECT age FROM table3;
```


### 4. 判断
通过 `if` 生成逻辑分支脚本（暂不支持 if 嵌套）


示例1:
```sql
define a 8

{% if $a > 4 %}
    SELECT * FROM table1;
{% endif %}
```

编译生成 sql 为:
```sql
SELECT * FROM table1;
```

示例2:
```sql
{% for n in table1,table2,table3 %}
    {% if $n == table1 %}
        SELECT id, name FROM {n};
    {% else%}
        SELECT * FROM {n};
    {% endif %}
{% endfor %}
```

编译生成 sql 为:
```sql
SELECT id, name FROM table1;
SELECT * FROM table2;
SELECT * FROM table3;
```


更多示例可参考 [demo.sqlx](https://github.com/taojy123/sqlx/blob/master/demo.sqlx)


### 5. 生成 `{` `}` 字符
如果你需要在生成的 sql 内容中包含 `{` `}` 这样的字符，不能直接在 sqlx 中写 `{` 或 `}`，因为这样会被认为是变量的引用标记

你需要在这些字符前加上一个转义符（默认是`\`），如 `\{` `\}` 这样即可

示例:
```sql
define cc dd
SELECT * FROM table1 WHERE name = 'aa\{bb\}{cc}'
```

编译生成 sql 为:
```sql
SELECT * FROM table1 WHERE name = 'aa{bb}dd'
```


### 6. 使用 `import` 导入模块

通过 import 可以引入现有的 sqlx 脚本文件作，但只能导入其中的 define 和 block

如果在当前脚本有重复同名变量或 block，会被覆盖以当前脚本为准

示例:
```sql
-- mod.sqlx
define colume  name
define colume2 score

block good_students(score)
    (
        SELECT
            *
        FROM
            students
        WHERE
            score > {score}
    ) AS good_students
endblock
```

```sql
import mod
define colume2 age
SELECT {colume} from teachers WHERE {colume2} > 10;
SELECT name FROM {good_students(60)};
SELECT count(*) FROM {good_students(80)};
```

编译生成 sql 为:
```sql
SELECT name from teachers WHERE age > 10;
SELECT name FROM 
    (
        SELECT
            *
        FROM
            students
        WHERE
            score > 60
    ) AS good_students
;
SELECT count(*) FROM 
    (
        SELECT
            *
        FROM
            students
        WHERE
            score > 80
    ) AS good_students
;
```


-------

## 使用方法

`Windows 64位系统`，直接下载 [sqlx.exe](https://github.com/taojy123/sqlx/releases) 放置于 `.sqlx 脚本文件` 同目录下

双击 `sqlx.exe` 即可在 `dist` 目录中生成对应 `sql` 文件


-------


## 其他系统平台，通过 Python3 安装使用

如果你的系统无法运行 `sqlx.exe`，可以先安装 [Python3](https://www.python.org/downloads/)，然后使用 `pip` 命令一键安装

```
pip install sqlx
```


### 使用 `sqlx` 命令行工具

1. 安装后直接执行 `sqlx` 命令，可一键编译当前目录下的所有 `.sqlx 脚本文件`
```
$ ls
test1.sqlx    test2.sqlx

$ sqlx
dist/test1.sql built
dist/test2.sql built
Finish!

$ ls dist
test1.sql    test2.sql
```


2. `sqlx` 命令后跟随目录路径参数，可编译指定路径下的所有脚本
```
$ ls test
test3.sqlx    test4.sqlx

$ sqlx ./test/
test/dist/test3.sql built
test/dist/test4.sql built
Finish!

$ ls test/dist
test3.sql    test4.sql
```


3. `sqlx` 命令后跟随文件路径参数，可编译指定的单个脚本
```
$ sqlx ./test/test3.sqlx
test/dist/test3.sql built
Finish!

$ ls test/dist
test3.sql
```


### 在 Python3 程序中使用 `sqlx.build` 方法
```python
import sqlx

my_script = """
{% for n in table1,table2,table3 %}
    {% if $n == table1 %}
        SELECT id, name FROM {n};
    {% else %}
        SELECT * FROM {n};
    {% endif %}
{% endfor %}
"""

sql = sqlx.build(my_script, pretty=True)
print(sql)
```






## 版本更新说明 


### v0.1.1

第一个可用版本发布

- 支持 `escape` （默认`\`）
- 自动复制编译的 `sql` 进剪切板
- import sqlx 脚本功能


### v0.1.0

第一个可用版本发布

- 支持 `define` 语法
- 支持 `block` 语法
- 支持 `for` 语法
- 支持 `if`  语法

