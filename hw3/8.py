with open('namelist.txt', 'r') as r:
    all = r.read().split('\n')

str1 = str(input())
if len(str1)==3:
    pass

for student in all:
    each = student.split()
    if len(str1)==3 and (len(each)==3):
        if str1[0]==each[0][0] and str1[1]==each[1][0] and str1[2]== each[2][0]:
            print(each)
    else:
        if str1[0]==each[0][0] and str1[-1]==each[-1][0]:
            print(each)