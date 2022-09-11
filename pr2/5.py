str1 = str(input())
n = int(input())
arr = list(str1)
listt = []
for j in range(n):
    listt.append([])
    output = ""
    for i in range(len(arr)):
        if i%n==j:
            listt[j].append(arr[i])
    
    for k in listt[j]:
        output += k
    print(output)
    


        



