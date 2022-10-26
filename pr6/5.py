import mysql.connector as mysql
import datetime
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Esko28:)", 
    database = "test")


cursor = db.cursor()

def update_professor_experience(prof_id): 
    arr = ['Prof_id', 'Prof_name', 'Uni_id', 'Joining_date', 'Speciality', 'Salary', 'Experience']
    cursor.execute(f"SELECT Joining_date from professor WHERE Prof_id= '{prof_id}'")
    records1 = cursor.fetchall()
    date_arr=records1[0][0].split('-')
    days_now = 2020*365+10*30+13
    days = int(date_arr[0])*365+ int(date_arr[1])*30+int(date_arr[2])
    delta = (days_now - days)//365
    
    
    # for i in date_arr:
    #     out+=i
    # d1 = datetime.datetime.now()

    # d2 = datetime.datetime.strftime(out, "%Y%m%d").date()
    
    # x  = d1-d2
    # print(x)
    

    

    #cursor.execute(f"SELECT * from professor WHERE Prof_id= '{prof_id}'")

    #records2 = cursor.fetchall()
update_professor_experience(101) 
 
