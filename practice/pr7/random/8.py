import random 
import string
len = random.randint(1, 10)
out = "".join(random.choices(string.punctuation, k=len))
print(out)