import numpy as np 



def max_end(arr):
    max = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if int(arr[i][j])>=max:
                max = int(arr[i][j])
    return max

def find_element(k, arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if int(arr[i][j])==k:
                return [i, j]

def pass_min(n, array):
    if n == max_end(array):
        return 0
    else:
        a, b = find_element(n, array)
        c, d = find_element(n+1, array)
        return pass_min(n+1, array)+abs(c-a)+abs(d-b)

    


arr = np.array([ 
  list("00000"), 
  list("01006"), 
  list("02000"), 
  list("30050"), 
  list("00004") 
] )

arr2 = np.array([
    list("00020000"),
    list("01000000")
])

print(pass_min(1, arr))
print(pass_min(1, arr2))