import re
with open('big.txt', 'r') as r:
    all = r.read().split('\n')

cnt = 0
for line in all:
    words = line.split()
    for word in words:
        cnt+=1


def findall(pattern, arr:list):
    output = []
    for line in arr:
        words = line.split()
        for word in words:
            x = re.findall(pattern, word)
            if x:
                output.append(word)
    return output

pattern1 = r'ime$'
pattern2 = r'^.ave.*'
pattern3 = r'[rstlne]'
pattern4 = r'^[b-d f-h j-n p-t v-z]+$'
pattern5 = r'^[aeuioAEUIO]+$'

print(findall(pattern1, all))
print(findall(pattern2, all))
print(len(findall(pattern3, all)))
print(len(findall(pattern3, all))/cnt*100)
print(findall(pattern4, all))
print(findall(pattern5, all))

