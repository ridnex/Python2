L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
pattern = 'a**a****'

for i in L:
    condition = True
    for j in range(len(pattern)):
        if pattern[j]!='*' and pattern[j]!=i[j]:
            condition = False
            
            break
    if condition==True:
        print(i)