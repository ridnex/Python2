n = int(input())
output = ""
Big_list = []

first_str = str(input())
Big_list.append(list(first_str))
lenn_big_slov = len(Big_list[0])


for i in range(n-1):
    str1 = str(input())
    if len(str1)!=lenn_big_slov:
        str1+=" "
    Big_list.append(list(str1))
    

    
for j in range(lenn_big_slov):
    for i in range(n):
        output+=Big_list[i][j]

print(output)

    
