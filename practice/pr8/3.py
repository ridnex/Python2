import numpy as np
arr = np.array([1, 1, 0, 0, 0, 1, 0] )
def transform(arr):
    arr[arr == 0] = 2
    arr[arr == 1] = 0
    arr[arr == 2] = 1

cnt = 0
if arr[0]==0:
    cnt = 0
else:
    for i in range(len(arr)):
        if arr[i]==1:
            cnt+=1
            transform(arr)

print(cnt)