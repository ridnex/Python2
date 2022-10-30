import random
import string

str1 = string.ascii_lowercase + string.ascii_uppercase
arr = random.choices(str1, k=5)
out= ""
for i in arr:
    out+=str(i)
print(out)


