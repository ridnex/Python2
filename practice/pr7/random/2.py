import random
arr= []
while len(arr)<100:
    a = random.randint(1000000000, 9999999999)
    if a not in arr:
        arr.append(a)

output = random.sample(arr, 2)
print(output)

