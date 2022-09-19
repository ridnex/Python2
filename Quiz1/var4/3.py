
def findall(str1: str, ch :chr )-> list:
    arr = []
    j = 0
    for i in str1:
        if i == ch:
            arr.append((j))
        j+=1
    return arr

string_input = 'asghahjba'
char_input = 'a'
print(findall(string_input, char_input))