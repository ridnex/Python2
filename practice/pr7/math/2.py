import math
def prime(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n))):
        if n%i==0:
            cnt+=1
    if cnt == 1:
        return True
    return False

def quadrats(n):
    k = int(math.sqrt(n))
    if k*k==n:
        return k
    return -1

def S_n(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n))+1):
        if quadrats(n-i**2)>=i:
            cnt+=i

    return cnt

for i in range(1, 37):
    cnt = 0
    n = i*4+1
    if prime(n)==True:
        cnt+=S_n(n)
print(cnt)
