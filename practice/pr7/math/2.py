#Integral median
import math
n = int(input())

def num_triangles(n):
    cnt = 0
    for c in range(1, n+1):
        for b in range(1, c+1):
            for a in range(1, b+1):
                if a+b>c:
                    if 2*a**2+2*b**2-c**2>=0:
                        M_c = 0.5 * math.sqrt(2*a**2+2*b**2-c**2)
                        if M_c.is_integer():
                            cnt +=1
    return cnt
    
print(num_triangles(n))