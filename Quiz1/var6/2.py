import math
x = int(input())
y = int(input())

try:
    print(math.sqrt(x-math.sqrt(y)))
except:
    print('plz enter valid numbers')