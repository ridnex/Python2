import numpy as np 
import math
array = [1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]]
element = 2
dic = {}
def freq_count(array, element, h=0):
    if len(array)==0:
        pass
    else:
        cnt = array.count(element)
        try:
            
            dic[h]=dic[h]+cnt
        except:
            dic[h]=cnt
        for i in array:
            if type(i)==type([]):
                freq_count(i, element, h+1)
freq_count(array, element)
arr = []
for i in dic.keys():
    out = []
    out.append(i)
    out.append(dic[i])
    arr.append(out)
print(arr)  


