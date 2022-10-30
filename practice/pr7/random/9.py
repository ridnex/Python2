import random
import string
out=''
lens= random.randint(2, 10)
while(len(out)!=lens):
    i = random.choices(string.ascii_lowercase, k=1)
    if i[0] not in out:
        out += str(i[0])

print(out)
