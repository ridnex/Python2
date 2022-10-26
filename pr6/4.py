import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Esko28:)", 
    database = "test")


cursor = db.cursor()

def get_prof(university_id:int): 
    cursor.execute(f"SELECT Prof_name from professor WHERE Uni_id = '{university_id}' ")
    records2 = cursor.fetchall()
    print(records2)
    cursor.execute(f"SELECT University_name from university WHERE University_id = '{university_id}' ")
    records3 = cursor.fetchall()

    print('University name:', records3[0][0])
    
get_prof(2)