str = str(input()).upper()
arr = []
for i in str:
    if i != " " and i!='.' and i != "?" and i!=',' and i != "!" and i!=':':
        arr.append(ord(i)-64)

print(arr)