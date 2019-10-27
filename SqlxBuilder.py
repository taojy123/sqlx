
import os
import sys

import sqlx


if 'pretty' in sys.argv:
    pretty = True
else:
    pretty = False


files = os.listdir('.')
files = [file for file in files if file.endswith('.sqlx')]


if not os.path.isdir('dist'):
    os.mkdir('dist')


for file in files:
    # change xx.sqlx to xx.sql
    new_file = os.path.join('dist', file[:-1])
    content = open(file, encoding='utf8').read()
    content = sqlx.build(content, pretty=pretty)
    open(new_file, 'w').write(content)
    print(f'{new_file} built')


print('Finish!')


