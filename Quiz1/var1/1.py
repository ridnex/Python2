import math
a = int(input())
b = int(input())
c = int(input())
d = b**2 - 4*a*c
if d<0:
    print('no root')
else:
    ans1 = (-b+math.sqrt(d))/(2*a)
    ans2 = (-b-math.sqrt(d))/(2*a)
    print(ans1, ans2)