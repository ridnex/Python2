import random

arr = [int(x) for x in range(100, 1000) if x%5==0]
print(random.choice(arr))