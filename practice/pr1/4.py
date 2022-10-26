arr = [str(x) for x in input().split(" ")]
set = {}
list = []
for i in arr:
    cnt = 0
    for j in range(len(arr)):
        if i == arr[j]:
            cnt+=1
    list.append(cnt)
    set[i]=cnt
list.sort()
for i in set.keys():
    if set[i] == list[-1]:
        print(i)

