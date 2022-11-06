#Jumping frog
import itertools 

def F(n):
    arr = []
    for i in range(1,n+1):
        arr.append(i)

    permut_arr = list(itertools.permutations(arr))
    cnt = 0
    for permut in permut_arr:
        if permut[0]==1 and permut[-1]==n:
            cond = True
            for i in range(len(permut)-1):
                if permut[i]-permut[i+1]>3 or permut[i]-permut[i+1]<-3 :
                    cond = False
                    break
            if cond:
                cnt+=1
    return cnt

def S(L):
    Sum = 0
    for n in range(1, L+1):
        Sum+= F(n)**3
    return Sum
L = int(input())
print(S(L))





