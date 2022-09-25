with open('students.txt', 'r') as r:
    all = r.read().split('\n')

with open('students2.txt', 'w')as w:
    for student in all:
        each = student.split()
        w.write(each[0][0].upper()+each[0][1:]+" "+each[1][0].upper()+each[1][1:]+' '+each[2]+" "+'301-'+each[-1])
        w.write('\n')


    
