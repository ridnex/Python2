for i in range(100,1000):
    d = i%10 #last
    m = i//100 #first
    k = (i-m*100)//10 #second
    if i==d**3+m**3+k**3:
        print(i)