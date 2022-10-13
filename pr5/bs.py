import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Esko28:)", 
    database = "test")


cursor = db.cursor()
#cursor.execute("CREATE DATABASE test")

#databases = cursor.fetchall() ## it returns a list of all databases present
#cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")
#cursor.execute("DROP TABLE users")
#cursor.execute("CREATE TABLE users (name VARCHAR(255), password INT)")
#query = "INSERT INTO users (name, password) VALUES (%s, %s)"
#values = ("Esko", 156464)
#cursor.execute(query, values)
cursor.execute('SELECT name FROM users where password=%s',)
table = cursor.fetchall() ## it returns a list of all databases present

print(table)
