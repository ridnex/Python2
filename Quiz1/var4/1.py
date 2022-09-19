arr = [int(x) for x in input().split()]
second_arr = [int(x) for x in arr if x%2==1]
second_arr.sort()
if len(second_arr)==0:
    print('not found')
else:
    print(second_arr[0])