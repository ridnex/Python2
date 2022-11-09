import numpy 
import re

pattern = r'^[a-z]{9}$'

def secret_password(pasw: str):
    x = re.findall(pattern, pasw)
    if len(x)==0:
        return "BANG! BANG! BANG!"
    else:
        pr1 = pasw[:3]
        pr2 = pasw[3:6]
        pr3 = pasw[6:]
        pr1=str(ord(pr1[0])-96)+pr1[1]+str(ord(pr1[-1])-96)

        pr2 = pr2[::-1]
        
        new_pr3 = ""
        for i in pr3:
            if ord(i)==ord('z'):
                new_pr3 += 'a'
            else:
                new_pr3 += chr(ord(i)+1)
        return pr2+new_pr3+pr1

def decoder(pasw: str):
    pr2 = pasw[:3]
    pr3 = pasw[3:6]
    pr1 = pasw[6:]
    pr2 = pr2[::-1]
    num = ""
    new_pr1 = ""
    for i in range(len(pr1)):
        if i == len(pr1)-1:
            
            num+=str(int(pr1[i]))
            new_pr1+=chr(int(num)+96)
        else:
            try:
                num+=str(int(pr1[i]))
            except:
                new_pr1 += chr(int(num)+96)+str(pr1[i])
                num=""
    new_pr3 = ""
    for i in pr3:
        if ord(i)==ord('a'):
            new_pr3 += 'z'
        else:
            new_pr3 += chr(ord(i)-1)
    return new_pr1+pr2+new_pr3

print(secret_password("mattedabi"))
print(decoder('detbcj13a20'))




