n = int(input())
cnt = 0
for i in range(1,n+1):
    qwe= 1
    for j in range(i, 2*i+1):
        qwe *=j
    cnt += qwe
print(cnt)
