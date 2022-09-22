with open('class_scores.txt', 'r') as f:
    all = f.read().split('\n')

with open('new_class_scores.txt', 'w') as k:

    for i in all:
        each = i.split()
        name = each[0]
        point = int(each[1])+5
        k.write(name + " "+str(point) +'\n')

