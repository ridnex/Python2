with open('file.txt', 'r') as f:
    all = f.read().split('\n')

output = []

for student in all:
    each = student.split(',')
    enter = each[1].split(":")
    enter_h = enter[0]
    enter_m = enter[1]
    out = each[2].split(":")
    out_h = out[0]
    out_m = out[1]
    enter_time = int(enter_h)*60 + int(enter_m)
    out_time = int(out_h)*60 + int(out_m)
    delta = out_time-enter_time
    if delta >= 60:
        print(each[0])

     