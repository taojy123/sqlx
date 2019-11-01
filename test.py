import sqlx

my_script = r"""
define cc dd
SELECT * FROM table1 WHERE name = 'aa\{bb\}{cc}'
"""

sql = sqlx.build(my_script)
print(sql)