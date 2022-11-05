from string import * 
from random import * 
letters = ascii_letters 
digits = digits 
#special_chars = punctuation 
t=letters+digits 
while True: 
    password = ''.join(choice(t) for i in range(10)) 
    if (sum(c.isdigit() for c in password)>=4): 
        break 
print(password)