n = int(input())

d = n%10 #last
m = n//100 #first
k = (n-m*100)//10

if d>=k and k>=m:
    print(True)
else:
    print(False)