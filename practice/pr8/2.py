import numpy as np

arr = np.array([ 

  [2, 0, 0],  

  [1, 1, 1],  

  [2, 2, 2] 

] )

def see_front(arr):
    arr2 = np.transpose(arr)
    for litle_arr in arr2:
        for i in range(len(litle_arr)-1):
            if litle_arr[i]>litle_arr[i+1]:
                return False
    return True

print(see_front(arr))