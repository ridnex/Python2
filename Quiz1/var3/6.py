arr = [1, 2, 3, 4, 5, 6, 7]
t = int(arr[0])
for i in range(0, len(arr)):
    if i == len(arr)-1:
        arr[i] = t
    else:
        arr[i] = arr[i+1]

print(arr)