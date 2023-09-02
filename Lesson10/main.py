from dbcontext import DBContext
context = DBContext("students.sl3", 5)
#1 Create table
#context.Query("CREATE TABLE S2016 (id INT PRIMARY KEY, name VARCHAR(20), age INT, avg_grade FLOAT)")
#2 Insert
#context.Query("INSERT INTO S2016 (id, name, age, avg_grade) VALUES(1, 'Vasylenko Andrii', 13, 11.5)")
#context.Query("INSERT INTO S2016 (id, name, age, avg_grade) VALUES(2, 'Marchenko Radomyr', 13, 8.5)")
#context.Query("INSERT INTO S2016 (id, name, age, avg_grade) VALUES(3, 'Sulskiy Ivan', 12, 11)")
#context.Query("INSERT INTO S2016 (id, name, age, avg_grade) VALUES(4, 'Kryzhanivskiy Daniil', 15, 11)")
#3 Update
#context.Query("UPDATE S2016 SET avg_grade = 9 WHERE id=2")
#4 Delete
#4.1
#context.Query("INSERT INTO S2016 (id, name, age, avg_grade) VALUES(5, 'test', 0, 0)")
#4.2
#context.Query("DELETE FROM S2016 WHERE id=5")
#5 Select
#res = context.Execute("SELECT * FROM S2016")
#res = context.Execute("SELECT id, name, age, avg_grade FROM S2016")
#res = context.Execute("SELECT name FROM S2016 WHERE avg_grade > 10")#DEFAULT -> DESC
#5.1 ORDER BY (ASC)
#res = context.Execute("SELECT name FROM S2016 WHERE avg_grade > 10 ORDER BY avg_grade ASC")
#res = context.Execute("SELECT name FROM S2016 ORDER BY avg_grade ASC")
#print(res)
#6 DROP TABLE
#context.Query("CREATE TABLE S2016SECOND (id INT PRIMARY KEY, name VARCHAR(20), age INT, avg_grade FLOAT)")
#context.Query("DROP TABLE S2016SECOND")