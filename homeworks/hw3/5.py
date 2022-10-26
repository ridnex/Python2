import re
n = int(input())
output = []
for i in range(n):
    a, b = [str(x) for x in input().split()]
    pattern = r'^<[a-z]+(.|_|\w)@[a-z]+\.[a-z]{2,3}>$'
    x = re.findall(pattern, b)
    if x:
        output.append(a+" "+b[1:-1])
for j in output:
    print(j)