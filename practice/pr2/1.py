arr = [int(x) for x in input().split(" ")]

if len(arr) == len(set(arr)):
    print(True)
else:
    print(False)