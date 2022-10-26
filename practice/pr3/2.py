import re

#a
with open('wordlist.txt', 'r') as f:
    all = f.read()
    
patternA = r'ime$'
x = re.findall(patternA, all)
print(x)

