from asyncio.windows_events import NULL
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Esko28:)", 
    database = "test")


cursor = db.cursor()

#cursor.execute("CREATE TABLE UNIVERSITY (University_id  INT, University_name  VARCHAR(255), Students_count INT)")
query = "INSERT INTO UNIVERSITY (University_id, University_name, Students_count) VALUES (%s, %s, %s)"
values = (1, "KBTU", 1230)
values1 =(2, 'KazNU', 10500)
values2 = (3, 'Kimep', 800)
values3 = (4, 'ATU', 958)
#cursor.execute(query, values)
#cursor.execute(query, values1)
#cursor.execute(query, values2)
#cursor.execute(query, values3)


#cursor.execute("CREATE TABLE professor(Prof_id INT, Prof_name VARCHAR(255), Uni_id INT, Joining_date VARCHAR(255), Speciality VARCHAR(255), Salary INT, Experience VARCHAR(255))")
P_query = "INSERT INTO professor(Prof_id, Prof_name, Uni_id, Joining_date, Speciality, Salary, Experience ) VALUES (%s, %s, %s, %s, %s, %s, %s)"
P_values = (101, 'Zedan', 1, '2005-02-10', 'Math', 3000,'NULL')
P_values1 =(102, 'Bekham',1, '2010-08-30', 'Physics', 3200,'NULL')
P_values2 = (103, 'Messi', 3, '2009-05-17', 'Chemistry', 4000,'NULL')
P_values3 = (104, 'Habib', 3, '2006-11-11', 'Math', 5000,'NULL')
P_values4 =(105, 'Ronaldo', 2, '2014-12-07', 'History', 1000,'NULL')
P_values5 = (106, 'Neimar', 2, '2011-04-23', 'Chemistry', 1500,'NULL')
P_values6 = (107,'Silva', 4, '2020-09-01', 'Baking', 800,'NULL')

cursor.execute(P_query, P_values)
cursor.execute(P_query, P_values1)
cursor.execute(P_query, P_values2)
cursor.execute(P_query, P_values3)
cursor.execute(P_query, P_values4)
cursor.execute(P_query, P_values5)
cursor.execute(P_query, P_values6)

db.commit()