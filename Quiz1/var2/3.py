str1 = str(input())
arr = list(str1)
arr_set = set(arr)
for i in arr_set:
    print(i, arr.count(i))
