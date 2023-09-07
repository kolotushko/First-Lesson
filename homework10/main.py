from dbcontext import DBContext
context = DBContext("datetimewind", 5)
context.Query("CREATE TABLE DateTimeWind (id INT PRIMARY KEY, date SEPTEMBER (07), time INT, avg_wind FLOAT)")
