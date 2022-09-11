import random

def sravnit2(a:chr, b:chr)->chr:
    if (a == "k" and b == "k") or (a == "n" and b == "n") or (a == "b" and b == "b"):
        return "q"
    elif (a == "k" and b == "n") or (a == "n" and b == "b") or (a == "b" and b == "k"):
        return a
    else:
        return b

def sravnit(a:chr, b:chr)->chr:
    if a == "k":
        if b == "n":
            return a
        if b == "b":
            return b
        else:
            return "q"
    
    if a == "b":
        if b == "n":
            return b
        if b == "b":
            return "q"
        else:
            return a
    
    if a == "n":
        if b == "n":
            return "q"
        if b == "b":
            return a
        else:
            return b
    
    



arr = ["k", "n", "b"]
atr1 = str(input())
str2 = (random.choice(arr))
print(str2)
ret = sravnit2(atr1, str2) 

if ret == "q":
    print("same")
elif ret == atr1:
    print("Human wins")
else:
    print("rand wins")
