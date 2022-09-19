n = int(input())

d = n%10 #last
m = n//100 #first
k = (n-m*100)//10

cnt = d*100 + k*10 +m
print(cnt)


