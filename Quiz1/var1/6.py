arr = [1,2,3,4,5,6,7]
t= arr[-1]
for i in range(len(arr)-1,-1,-1):
    if i==0:
        arr[i]=t
    else:
        arr[i]=arr[i-1]
print(arr)