a1 = [int(x) for x in input().split(" ")]
a2 = [int(x) for x in input().split(" ")]
a3 = [int(x) for x in input().split(" ")]
matrix = [a1, a2, a3]

def matrix22(matrix2:list) -> int:
    return matrix2[3]*matrix2[0]-matrix2[1]*matrix2[2]

diogonal = []
for i in range(3):
    diogonal.append(matrix[i][i])
    
list_of22 = []
for k in range(3):
    list = []
    for i in range(3):
        for j in range(3):
            if i!=k and j!=k:
                list.append(matrix[i][j])
    list_of22.append(list)
cnt = 0
print(list_of22)
for k in range(3):
    if k!=1:
        cnt += diogonal[k]*matrix22(list_of22[k])
    else:
        cnt += -1*diogonal[k]*matrix22(list_of22[k])


print(cnt)
    
    

            


