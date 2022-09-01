str = str(input()).upper()
arr = []
for i in str:
    if i != " ":
        arr.append(ord(i)-64)

print(arr)