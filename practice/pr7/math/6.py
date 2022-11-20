#Guessing Game

def mid_point(n, a, b):
    cnt = 0
    num = n//2
    if a>=b:
        points = n
    else:
        points = 1
    while points!=num:
        if points<num:
            num=(1+num)//2
            cnt+=b
        else:
            num = (n+ num)//2
            cnt+=a
    if points<num:
        num=(1+num)//2
        cnt+=b
    else:
        num = (n+ num)//2
        cnt+=a
    return cnt

print(mid_point(5,2,3))
    

