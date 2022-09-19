import math
x, y = 0, 0
a = str(input())
while a != '0':

    arr_str = [str(x) for x in a.split(' ')]
    cancole = arr_str[0]
    step = int(arr_str[1])
    if cancole == "UP":
        y += step
    elif cancole == "DOWN":
        y -= step
    elif cancole == "LEFT":
        x -= step
    else:
        x+=step
    a = str(input())
dist = math.sqrt(x**2 + y**2)
print(dist)
print(int(dist+0.5))
