arr = [int(x) for x in input().split(" ")]
all = set(arr)
for i in all:
    arr.remove(i)
    if i not in arr:
        print(i)


        
    
    
