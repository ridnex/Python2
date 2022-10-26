n = int(input())
output= []
import re
def valid(str1):
    cnt = 0
    pattern = r'^[4,5,6]\d{3}-?\d{4}-?\d{4}-?\d{4}$'
    arr = list(str1)
    for i in range(len(arr)-1):
        if arr[i]=="-":
            if arr[i-1]==arr[i+1]:
                cnt+=1
            else:
                cnt=0
        else:
            if arr[i]==arr[i+1]:
                cnt+=1
            elif arr[i+1]=='-':
                pass
            
            else:
                cnt=0

        if cnt == 3:
            return False
    
    x = re.findall(pattern, str1)
    if x :
        return True
    return False
        
for i in range(n):
    str1 = str(input())
    if valid(str1)==True:
        output.append('Valid')
    else:
        output.append("Invalid")

for j in output:
    print(j)