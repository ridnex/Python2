import math
from re import sub

def sum_10(n:str):
    cnt =0
    for i in n:
        cnt+= int(i)
    return cnt


def sub_10(number_string):
    out = ''
    for i in range(len(number_string)-1):
        arr = (number_string[i])
        for j in range(i+1, len(number_string)):
            if sum_10(arr)>10:
                arr=''
                break
            else:
                arr+= str(number_string[j])
                if sum_10(arr)==10:
                    out+=arr
                    arr = ""
                    break
    for i in number_string:
        if i not in out:
            return False
        
    return(True)
print(sub_10('9461111'))
# m = int(input())
# cnt = 0
# for n in range(1, 10**m+1):
#     if sub_10(str(n))==True:
#         cnt+=1
# print(cnt)
    



