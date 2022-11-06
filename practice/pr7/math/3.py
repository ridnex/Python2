#Triangle on parabola
import math

def coord(a, b, c, k):
    a_lenth = math.sqrt((b-c)**2+(b**2/k-c**2/k)**2)
    b_lenth = math.sqrt((a-c)**2+(a**2/k-c**2/k)**2)
    c_lenth = math.sqrt((a-b)**2+(a**2/k-b**2/k)**2)
    p = (a_lenth + b_lenth + c_lenth)/2
    
    area = math.sqrt(p*(p-a_lenth)*(p-b_lenth)*(p-c_lenth))
    if int(area) == int(0.5 * a * b * (math.sqrt(2)/2)):
        return True
    if int(area) == int(0.5 * c * b * (math.sqrt(2)/2)):
        return True
    if int(area) == int(0.5 * a * c *( math.sqrt(2)/2)):
        return True
    print(area)
    return False

def F(K, X):
    cnt = 0
    for k in range(1, K+1):
        for c in range(-X,X+1):
            for b in range(-X, c):
                for a in  range(-X, b):
                    if coord(a, b, c, k):
                        cnt += 1
    return cnt

X = int(input('X:'))
K = int(input('K:'))
print(F(K, X))



