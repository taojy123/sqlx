# sqlx
SQL Extension
一种扩展 sql 的语言，目标是打造 "易读易写 方便维护" 的 sql 脚本


## 安装
`Windows` 系统直接下载 `SqlBuilder.exe` 即可



## 语法简介

1. 变量替换
```
define 变量名 变量值

{变量名}
```

示例 sqlx:
```
define a id
define b name
define c students

SELECT {a}, {b} FROM {c} WHERE {a} > 10
```

编译生成 sql:
```
SELECT id, name FROM students WHERE id > 10
```


2. 利用片段（block）来批量生成脚本
定义片段
```
block 片段名(参数名)
    片段内容
endblock

{片段名(参数值)}
```

在 sqlx 中可以直接已定义片段并传入相应的参数
示例如下：
```
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

SELECT 
    name 
FROM 
    {good_students(80)}
```

编译生成 sql:
```
SELECT 
    name 
FROM 
    (
        SELECT
            *
        FROM
            students
        WHERE
            score > {score}
    ) AS good_students
```


3. 循环
```
{% for 循环变量名 in 循环变量值 %}
    循环体
{% endfor %}
```


示例 sqlx:
```
{% for n in table1,table2,table3 %}
    SELECT * FROM {n};
{% endfor %}
```

编译生成 sql:
```
SELECT * FROM table1;
SELECT * FROM table2;
SELECT * FROM table3;
```


4. 判断
```
{% if 判断条件 %}
    判断为真 对应代码
{% else% }
    判断为假 对应代码
{% endif %}
```


示例 sqlx:
```
{% for n in table1,table2,table3 %}
    {% if n == table1 %}
        SELECT id, name FROM {n};
    {% else% }
        SELECT * FROM {n};
    {% endif %}
{% endfor %}
```

编译生成 sql:
```
SELECT id, name FROM table1;
SELECT * FROM table2;
SELECT * FROM table3;
```




在 `Python3` 环境下，可以使用 `pip` 一键安装
```
pip install sqlx
```
