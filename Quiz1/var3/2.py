n = int(input())
n1 = n
arr = []
while n1>0:
    arr.append(n1%10)
    n1 = n1 // 10
cnt = 0
arr.reverse()
for i in range(len(arr)):
    cnt += arr[i]*(10**i)

if cnt == n:
    print('YES')
else:
    print('NO')