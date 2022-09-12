row= int(input())
column = int(input())
matrix = []
row1 = row // 2
row2 = row - row1 

#1  part
for i in range(row1):
    rowi = []
    for j in range(column):
        if ((i==0 or i==row1-1) and j!=column-1) or ((i!= 0 and i!= row1-1) and (j==0 or j == column-1)):
            rowi.append('*')
        else:
            rowi.append(' ')
    matrix.append(rowi)
    for k in rowi:
        print(k, end = " ")
    print()  

#2 part
for i in range(row2):
    rowi = []
    for j in range(column):
        if j==0 or (i+1==j):
            rowi.append('*')
        else:
            rowi.append(' ')
    matrix.append(rowi)
    for k in rowi:
        print(k, end = " ")
    print()     
