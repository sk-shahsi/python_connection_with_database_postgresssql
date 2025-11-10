this are commonaly used command
postsql

Microsoft Windows [Version 10.0.26100.6899]
(c) Microsoft Corporation. All rights reserved.

D:\vs for python>pip install virtualenv
Collecting virtualenv
  Downloading virtualenv-20.35.4-py3-none-any.whl.metadata (4.6 kB)
Collecting distlib<1,>=0.3.7 (from virtualenv)
  Downloading distlib-0.4.0-py2.py3-none-any.whl.metadata (5.2 kB)
Collecting filelock<4,>=3.12.2 (from virtualenv)
  Downloading filelock-3.20.0-py3-none-any.whl.metadata (2.1 kB)
Collecting platformdirs<5,>=3.9.1 (from virtualenv)
  Downloading platformdirs-4.5.0-py3-none-any.whl.metadata (12 kB)
Downloading virtualenv-20.35.4-py3-none-any.whl (6.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.0/6.0 MB 8.1 MB/s eta 0:00:00
Downloading distlib-0.4.0-py2.py3-none-any.whl (469 kB)
Downloading filelock-3.20.0-py3-none-any.whl (16 kB)
Downloading platformdirs-4.5.0-py3-none-any.whl (18 kB)
Installing collected packages: distlib, platformdirs, filelock, virtualenv
Successfully installed distlib-0.4.0 filelock-3.20.0 platformdirs-4.5.0 virtualenv-20.35.4

[notice] A new release of pip is available: 24.3.1 -> 25.3
[notice] To update, run: python.exe -m pip install --upgrade pip

D:\vs for python>virtualenv env
created virtual environment CPython3.13.2.final.0-64 in 12173ms
  creator CPython3Windows(dest=D:\vs for python\env, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=C:\Local\pypa\virtualenv)
    added seed packages: pip==25.3
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

D:\vs for python>cd env

D:\vs for python\env>cd scripts

D:\vs for python\env\Scripts>activate

(env) D:\vs for python\env\Scripts>cd ..

(env) D:\vs for python\env>cd ..

(env) D:\vs for python>python test.py
hello world

(env) D:\vs for python>de^A




Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
Password for user postgres:

psql (18.0)
WARNING: Console code page (437) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

postgres=# \l
                                                            List of databases
   Name    |  Owner   | Encoding | Locale Provider |      Collate       |       Ctype        | Locale | ICU Rules |   Access privileges
-----------+----------+----------+-----------------+--------------------+--------------------+--------+-----------+-----------------------
 postgres  | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           |
 template0 | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           | =c/postgres          +
           |          |          |                 |                    |                    |        |           | postgres=CTc/postgres
 template1 | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           | =c/postgres          +
           |          |          |                 |                    |                    |        |           | postgres=CTc/postgres
(3 rows)


postgres=# create database demodb;
CREATE DATABASE
postgres=# \l
                                                            List of databases
   Name    |  Owner   | Encoding | Locale Provider |      Collate       |       Ctype        | Locale | ICU Rules |   Access privileges
-----------+----------+----------+-----------------+--------------------+--------------------+--------+-----------+-----------------------
 demodb    | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           |
 postgres  | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           |
 template0 | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           | =c/postgres          +
           |          |          |                 |                    |                    |        |           | postgres=CTc/postgres
 template1 | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           | =c/postgres          +
           |          |          |                 |                    |                    |        |           | postgres=CTc/postgres
(4 rows)


postgres=# \c demodb
You are now connected to database "demodb" as user "postgres".
demodb=# create database test;
CREATE DATABASE
demodb=# \n
invalid command \n
Try \? for help.
demodb=# \l
                                                            List of databases
   Name    |  Owner   | Encoding | Locale Provider |      Collate       |       Ctype        | Locale | ICU Rules |   Access privileges
-----------+----------+----------+-----------------+--------------------+--------------------+--------+-----------+-----------------------
 demodb    | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           |
 postgres  | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           |
 template0 | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           | =c/postgres          +
           |          |          |                 |                    |                    |        |           | postgres=CTc/postgres
 template1 | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           | =c/postgres          +
           |          |          |                 |                    |                    |        |           | postgres=CTc/postgres
 test      | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           |
(5 rows)


demodb=# drop database test;
DROP DATABASE
demodb=# \l
                                                            List of databases
   Name    |  Owner   | Encoding | Locale Provider |      Collate       |       Ctype        | Locale | ICU Rules |   Access privileges
-----------+----------+----------+-----------------+--------------------+--------------------+--------+-----------+-----------------------
 demodb    | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           |
 postgres  | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           |
 template0 | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           | =c/postgres          +
           |          |          |                 |                    |                    |        |           | postgres=CTc/postgres
 template1 | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           | =c/postgres          +
           |          |          |                 |                    |                    |        |           | postgres=CTc/postgres
(4 rows)


demodb=# cd..
demodb-# cd.
demodb-# \c database postgres
connection to server at "localhost" (::1), port 5432 failed: FATAL:  database "database" does not exist
Previous connection kept
demodb-# create database student;
ERROR:  syntax error at or near "cd"
LINE 1: cd..
        ^
demodb=# create database student;
CREATE DATABASE
demodb=# create table student(name text,number int,age int);
CREATE TABLE
demodb=# \d
          List of relations
 Schema |  Name   | Type  |  Owner
--------+---------+-------+----------
 public | student | table | postgres
(1 row)


demodb=# INSERT INTO student(name,number,age) values('puja',90,25);
INSERT 0 1
demodb=# INSERT INTO student(name,number,age) values('aashish',91,28);
INSERT 0 1
demodb=#
demodb=#
demodb=#
demodb=#
demodb=#
demodb=#
demodb=#
demodb=#
demodb=# select * from student;
  name   | number | age
---------+--------+-----
 puja    |     90 |  25
 aashish |     91 |  28
(2 rows)


demodb=# select name from studen;
ERROR:  relation "studen" does not exist
LINE 1: select name from studen;
                         ^
demodb=# select name from student;
  name
---------
 puja
 aashish
(2 rows)


demodb=# select * from student where number=90;
 name | number | age
------+--------+-----
 puja |     90 |  25
(1 row)


demodb=# select number from student where age =25;
 number
--------
     90
(1 row)


demodb=# select number from student where name='aashish';
 number
--------
     91
(1 row)


demodb=# truncate table student;
TRUNCATE TABLE
demodb=# \d
          List of relations
 Schema |  Name   | Type  |  Owner
--------+---------+-------+----------
 public | student | table | postgres
(1 row)


demodb=# select * from student;
 name | number | age
------+--------+-----
(0 rows)


demodb=#







Microsoft Windows [Version 10.0.26100.6899]
(c) Microsoft Corporation. All rights reserved.

D:\vs for python>pip install virtualenv
Collecting virtualenv
  Downloading virtualenv-20.35.4-py3-none-any.whl.metadata (4.6 kB)
Collecting distlib<1,>=0.3.7 (from virtualenv)
  Downloading distlib-0.4.0-py2.py3-none-any.whl.metadata (5.2 kB)
Collecting filelock<4,>=3.12.2 (from virtualenv)
  Downloading filelock-3.20.0-py3-none-any.whl.metadata (2.1 kB)
Collecting platformdirs<5,>=3.9.1 (from virtualenv)
  Downloading platformdirs-4.5.0-py3-none-any.whl.metadata (12 kB)
Downloading virtualenv-20.35.4-py3-none-any.whl (6.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.0/6.0 MB 8.1 MB/s eta 0:00:00
Downloading distlib-0.4.0-py2.py3-none-any.whl (469 kB)
Downloading filelock-3.20.0-py3-none-any.whl (16 kB)
Downloading platformdirs-4.5.0-py3-none-any.whl (18 kB)
Installing collected packages: distlib, platformdirs, filelock, virtualenv
Successfully installed distlib-0.4.0 filelock-3.20.0 platformdirs-4.5.0 virtualenv-20.35.4

[notice] A new release of pip is available: 24.3.1 -> 25.3
[notice] To update, run: python.exe -m pip install --upgrade pip

D:\vs for python>virtualenv env
created virtual environment CPython3.13.2.final.0-64 in 12173ms
  creator CPython3Windows(dest=D:\vs for python\env, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=C\pypa\virtualenv)
    added seed packages: pip==25.3
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

D:\vs for python>cd env

D:\vs for python\env>cd scripts

D:\vs for python\env\Scripts>activate

(env) D:\vs for python\env\Scripts>cd ..

(env) D:\vs for python\env>cd ..

(env) D:\vs for python>python test.py
hello world

(env) D:\vs for python>pip install psycopg2==2.8.6
Collecting psycopg2==2.8.6
  Downloading psycopg2-2.8.6.tar.gz (383 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: psycopg2
  Building wheel for psycopg2 (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for psycopg2 (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [33 lines of output]
      C:\Users\eraas\AppData\Local\Temp\pip-build-env-ykniz5_4\overlay\Lib\site-packages\setuptools\dist.py:759: SetuptoolsDeprecationWarning: License classifiers are deprecated.
      !!

              ********************************************************************************
              Please consider removing the following classifiers in favor of a SPDX license expression:

              License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)

              See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
              ********************************************************************************

      !!
        self._finalize_license_expression()
      running bdist_wheel
      running build
      running build_py
      creating build\lib.win-amd64-cpython-313\psycopg2
      copying lib\compat.py -> build\lib.win-amd64-cpython-313\psycopg2
      copying lib\errorcodes.py -> build\lib.win-amd64-cpython-313\psycopg2
      copying lib\errors.py -> build\lib.win-amd64-cpython-313\psycopg2
      copying lib\extensions.py -> build\lib.win-amd64-cpython-313\psycopg2
      copying lib\extras.py -> build\lib.win-amd64-cpython-313\psycopg2
      copying lib\pool.py -> build\lib.win-amd64-cpython-313\psycopg2
      copying lib\sql.py -> build\lib.win-amd64-cpython-313\psycopg2
      copying lib\tz.py -> build\lib.win-amd64-cpython-313\psycopg2
      copying lib\_ipaddress.py -> build\lib.win-amd64-cpython-313\psycopg2
      copying lib\_json.py -> build\lib.win-amd64-cpython-313\psycopg2
      copying lib\_lru_cache.py -> build\lib.win-amd64-cpython-313\psycopg2
      copying lib\_range.py -> build\lib.win-amd64-cpython-313\psycopg2
      copying lib\__init__.py -> build\lib.win-amd64-cpython-313\psycopg2
      running build_ext
      building 'psycopg2._psycopg' extension
      error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for psycopg2
Failed to build psycopg2
error: failed-wheel-build-for-install

× Failed to build installable wheels for some pyproject.toml based projects
╰─> psycopg2

(env) D:\vs for python>pip install psycopg2
Collecting psycopg2
  Downloading psycopg2-2.9.11-cp313-cp313-win_amd64.whl.metadata (5.1 kB)
Downloading psycopg2-2.9.11-cp313-cp313-win_amd64.whl (2.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.7/2.7 MB 8.8 MB/s  0:00:00
Installing collected packages: psycopg2
Successfully installed psycopg2-2.9.11

(env) D:\vs for python>python test.py
Connection successful

(env) D:\vs for python>python test.py
Table created successfully
Connection successful

(env) D:\vs for python>pip install psycopg2
Requirement already satisfied: psycopg2 in d:\vs for python\env\lib\site-packages (2.9.11)

(env) D:\vs for python>where python
D:\vs for python\env\Scripts\python.exe
C:\Users\eraas\AppData\Local\Programs\Python\Python313\python.exe
C:\Users\eraas\AppData\Local\Microsoft\WindowsApps\python.exe

(env) D:\vs for python>python -m pip show psycopg2
Name: psycopg2
Version: 2.9.11
Summary: psycopg2 - Python-PostgreSQL Database Adapter
Home-page: https://psycopg.org/
Author: Federico Di Gregorio
Author-email: fog@initd.org
License: LGPL with exceptions
Location: D:\vs for python\env\Lib\site-packages
Requires:
Required-by:

(env) D:\vs for python>python test.py
Traceback (most recent call last):
  File "D:\vs for python\test.py", line 5, in <module>
    cursor.execute('''create table employee(Name text,Id int,Age int);''')
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.DuplicateTable: relation "employee" already exists


(env) D:\vs for python>python test.py
Table created successfully
Connection successful

(env) D:\vs for python>
