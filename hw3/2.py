with open('first.txt', 'r') as f:
    all1 = f.read().split('\n')
with open('second.txt', 'r')as k:
    all2 = k.read().split('\n')

with open('third.txt', 'w') as q:
    for i in range(len(all1)):
        q.write(all1[i]+" "+all2[i])
        q.write('\n')