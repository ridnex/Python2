# import re
# import random
# import string

# pattern = r'^(?=.*[a-z])(?=.+[A-Z])(?=.*\d)(?=.+[A-Z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10}$'
# out = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase+string.digits + string.punctuation, k=10))
# print(out)
# x = re.findall(pattern, out)
# print(x)
# while len(x)==0:
#     out = ""
#     out = ''.join(random.choices(string.ascii_uppercase +string.digits, k=10))
#     x = re.findall(out, pattern)

# print(out)

from string import * 
from random import * 
letters = ascii_letters 
digits = digits 
special_chars = punctuation 
t=letters+digits+special_chars 
while True: 
    password = ''.join(choice(t) for i in range(10)) 
    if (any(c.isdigit() for c in password) 
            and any(not c.isalnum() for c in password)  
            and sum(c.isupper() for c in password)>=2): 
        break 
print(password)
