import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Esko28:)", 
    database = "test")


cursor = db.cursor()

def get_specialist_professor_list(speciality:str, salary:int): 
    cursor.execute(f"SELECT * from professor WHERE (Speciality = '{speciality}' AND Salary >= '{salary}')")
    records2 = cursor.fetchall()
    arr = ['Prof_id', 'Prof_name', 'Uni_id', 'Joining_date', 'Speciality', 'Salary', 'Experience']

    print("Printing professors whose specialty is Chemistry and salary greater than 1500 ")
    for record in records2:
        for i in range(len(arr)):
            print(f'{arr[i]} : {record[i]}')


     
get_specialist_professor_list('Chemistry', 1500)

#db.commit()