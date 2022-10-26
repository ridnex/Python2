x = int(input())
y = int(input())
z = int(input())
if x == y and x == z:
    print('equilateral')
elif x!=y and y!=z and z!=x:
    print('scalene')
else:
    print('isosceles')

