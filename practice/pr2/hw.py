dic = {'A':'B', 'B':['C', 'D'], 'C':'G', 'D':['F', 'H', 'J']}
element = "C"
cnt = 0
while element !="A":
    for i in dic.keys():
        if element in dic[i] or dic[i] == element:
            element = i
            cnt += 1
            
print(cnt)
