import numpy as np

arr = np.array([ 

  [1, 2, 3, 6 ], 

  [4, 5, 6, 15], 

  [7, 8, 9, 24], 

  [12,15,18,46] 

]  )
def sum_elements(i, j, arr):
    if j == len(arr)-1:
        cnt = 0
        for k in arr[i][:-1]:
            cnt+=k
        print(cnt)
    else:
        cnt = 0
        for k in arr[i][:-1]:
            cnt+=k
        delta = (arr[i][-1]-cnt)
        print(arr[i][j]+delta)

        
for i in range(len(arr)):
    cnt = 0
    for elements in arr[i]:
        cnt+=elements
    if cnt != 2*arr[i][-1]:
        for j in range(len(arr[0])):
            column_arr = arr[:, j]
            col_cnt = 0
            for elements in column_arr:
                col_cnt+=elements
            if col_cnt != 2* column_arr[-1]:
                print(arr[i][j])
                sum_elements(i, j, arr)
                
            

        
    