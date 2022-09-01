astr = str(input())
ast = list(astr)
def index(strb:str) -> int:
    cnt=0
    for i in strb:
        if i=="o" or i=="a" or i=="e" or i =="i" or i == "y" or i=="u":
            return cnt
        cnt+=1
    return -1

index1 = index(astr)
if index1 >=0:
    ans = ""
    for i in range(0, index1):
        ans+=ast[i]
    wer = ""
    for i in range(index1, len(ast)):
        wer+=ast[i]
    print(wer+ans+"ay")
else:
    reverse_str = ""
    ast.reverse()
    for i in ast:
        reverse_str += i
    print(reverse_str+'ay')
