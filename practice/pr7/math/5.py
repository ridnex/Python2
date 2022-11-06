#10-substrings
import math

def sum_10(n:str):
    cnt =0
    for i in n:
        cnt+= int(i)
    return cnt


def sub_10(number_string):
    
    string_arr = list(number_string)
    out_ind = []
    for i in range(len(number_string)-1):
        string = (number_string[i])
        for j in range(i+1, len(number_string)):
            if sum_10(string)>10:
                
                string=''
                break
            
            else:
                string+= str(number_string[j])
                if sum_10(string)==10:
                    
                    for j in string:
                        for k in range(len(string_arr)):
                            if j==string_arr[k]:
                                out_ind.append(k)
                                string_arr[k]=-1
                                break
                    
                    string = ""
                    
                    break
    #print(out_ind)
    if len(out_ind)==len(number_string):
        return True
    return False
        
    

m = int(input())
cnt = 0
for n in range(1, 10**m+1):
    # qwe = str(n).split("0")
    # stri = ''
    # for i in qwe:
    #     stri+=i
    stri = ''
    qwe = str(n)
    for i in qwe:
        if i!='0':
            stri+=i

    if sub_10(stri)==True:
        cnt+=1
print(cnt)

    



