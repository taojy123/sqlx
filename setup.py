#coding=utf8

from setuptools import setup, find_packages

from sqlx import VERSION


try:
    long_description = open('README.md', encoding='utf8').read()
except Exception as e:
    long_description = ''


install_requires = []
for line in open('requirements.txt', encoding='utf8').readlines():
    line = line.strip()
    if line and not line.startswith('#'):
        install_requires.append(line)


setup(
    name='sqlx',
    version=VERSION,
    description='SQL Extension | SQL 语法拓展，目标是打造 "易读易写 方便维护" 的 sql 脚本',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='tao.py',
    author_email='taojy123@163.com',
    maintainer='tao.py',
    maintainer_email='taojy123@163.com',
    install_requires=install_requires,
    license='MIT License',
    packages=find_packages(),
    py_modules=['sqlx', 'sqlformat'],
    entry_points={
        'console_scripts': ['sqlx=sqlx:auto'],
    },
    include_package_data=True,
    platforms=["all"],
    url='https://github.com/taojy123/sqlx',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries'
    ],
)
