
def findall(str1: str, ch :chr )-> list:
    arr = []
    j = 0
    for i in str1:
        if i == ch:
            arr.append((j))
        j+=1
    return arr

def equal(str1:str, str2: str)->bool:
    if len(str1)!=len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            return False
        if findall(str1, str1[i]) != findall(str2, str2[i]):
            return False
    return True


str1 = str(input())
str2 = str(input())

print(equal(str1, str2))