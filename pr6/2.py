import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Esko28:)", 
    database = "test")


cursor = db.cursor()

def get_university_detail(u_id: int): 
    print('Printing University record :')
    arr = ['University_id', 'University_name', 'Students_count']
    cursor.execute(f"SELECT * from university WHERE University_id = {u_id}")
    records = cursor.fetchall()
    for record in records:
        for i in range(len(arr)):
            print(f'{arr[i]} : {record[i]}')


 

def get_prof_detail(p_id): 
    print('Printing Professor record :')
    arr = ['Prof_id', 'Prof_name', 'Uni_id', 'Joining_date', 'Speciality', 'Salary', 'Experience']
    cursor.execute(f"SELECT * from professor WHERE Prof_id = {p_id};")
    records2 = cursor.fetchall()
    for record in records2:
        for i in range(len(arr)):
            print(f'{arr[i]} : {record[i]}')


get_university_detail(2)
get_prof_detail(105)