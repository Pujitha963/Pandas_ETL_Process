# Pandas_ETL_Process
Simple Project to perform ETL operation

Created a database (pandas_practice) having a table student as below
+-----+-------+--------+------+
| id  | name  | gender | age  |
+-----+-------+--------+------+
| 101 | lucky | F      |   19 |
| 102 | sony  | F      |   18 |
| 103 | john  | M      |   20 |
| 104 | jack  | M      |   20 |
| 105 | lily  | F      |   18 |
+-----+-------+--------+------+

1. Created configuration file (config.py) to have the details of mysql database.
2. Extracted student data from student table in mysql using sqlalchemy.
3. Transformed data of students - renamed the columns id -> student_id and name -> student_name.
4. Loaded the trasformed data into csv file.
