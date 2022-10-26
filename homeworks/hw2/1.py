column = int(input())
row = int(input())
matrix = []
for i in range(column):
    rowi = []
    for j in range(row):
        
        if ((i!=0 and i!= column -1 )and(j==0 or j == row-1)) or ((i==0 or i==column-1) and (j!=0 and j != row-1)):
            rowi.append('*')
        else:
            rowi.append(' ')
    matrix.append(rowi)
    for k in rowi:
        print(k, end = " ")
    print()


