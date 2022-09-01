n = int(input())
for i in range(1,n):
    num = i
    j = 0
    while num > 0:
        num=num//10
        j += 1

    ten = 10**j

    if (i**2-i)%ten==0:
        print(i)
