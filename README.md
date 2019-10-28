# sqlx
SQL Extension
一种扩展 sql 的语言，目标是打造 "易读易写 方便维护" 的 sql 脚本


## 安装使用
`Windows` 系统直接下载 `SqlBuilder.exe` 放置于 `sqlx` 脚本同目录下
双击 `SqlBuilder.exe` 即可完成自动编译，生成 `sql` 文件


## 语法简介

1. 通过 `define` 定义变量，可在脚本中反复引用

示例:
```
define field_name age

SELECT {field_name} from students WHERE {field_name} > 10;
SELECT {field_name} from teachers WHERE {field_name} > 10;
```

对应编译生成的 sql 为:
```
SELECT age from students WHERE age > 10;
SELECT age from teachers WHERE age > 10;
```


2. 通过 `block` 定义脚本片段，并反复引用

示例:
```
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

对应编译生成的 sql 为:
```
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


3. 循环
通过 `for` 批量循环生成脚本（暂不支持循环嵌套）



示例1:
```
{% for n in table1,table2,table3 %}
    SELECT * FROM {n};
{% endfor %}
```

对应编译生成的 sql 为:
```
SELECT * FROM table1;
SELECT * FROM table2;
SELECT * FROM table3;
```


示例2:
```
{% for n|m in table1|id,table2|name,table3|age %}
    SELECT {m} FROM {n};
{% endfor %}
```

对应编译生成的 sql 为:
```
SELECT id FROM table1;
SELECT name FROM table2;
SELECT age FROM table3;
```


4. 判断
通过 `if` 生成逻辑分支脚本（暂不支持 if 嵌套）


示例1:
```
define a 8

{% if {a} > 4 %}
    SELECT * FROM table1;
{% endif %}
```

对应编译生成的 sql 为:
```
SELECT * FROM table1;
```

示例2:
```
{% for n in table1,table2,table3 %}
    {% if n == table1 %}
        SELECT id, name FROM {n};
    {% else% }
        SELECT * FROM {n};
    {% endif %}
{% endfor %}
```

对应编译生成的 sql 为:
```
SELECT id, name FROM table1;
SELECT * FROM table2;
SELECT * FROM table3;
```





## 安装 Python 模块
```
pip install sqlx
```


