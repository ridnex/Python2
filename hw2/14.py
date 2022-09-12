a = int(input())
sum = 0
cnt = 0
while(a!=0):
    sum += a
    cnt += 1
    a = int(input())
avr = sum / cnt
print(avr)
print(sum)