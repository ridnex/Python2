n = int(input())
cnt = 1+2
def fact(a:int):
    qwe = 1
    for i in range(1, a+1):
        qwe*=i
    return qwe

for i in range(3, n+1):
    cnt+=i*2*fact(i)
print(cnt)
