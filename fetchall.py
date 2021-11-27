import sqlite3
myschool=sqlite3.connect('test.db')
sql="SELECT * FROM students"
curschool=myschool.cursor()
curschool.execute(sql)
result=curschool.fetchall()
for record in result:
    print(record)
