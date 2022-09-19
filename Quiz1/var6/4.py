import re
arr = [str(x) for x in input().split(',')]

def correct(str1:str)->bool:
    if 6>len(str1) or len(str1)>12:
        return False

    x = re.findall(r'[A-Z]', str1)
    if len(x)==0:
        return False
    
    y = re.findall(r'\d', str1)
    if len(y)==0:
        return False
    
    z = re.findall(r'[a-z]', str1)
    if len(z)==0:
        return False
    
    v = re.findall(r'[$#@]', str1)
    if len(v)==0:
        return False
    return True

for i in arr:
    if correct(i):
        print(i)