Secter_word = "EVAPORATE"
output_string = []

def findall(str1: str, ch :str )-> list:
    arr = []
    j = 0
    for i in str1:
        if i == ch:
            arr.append((j))
        j+=1
    return arr


for i in range(len(Secter_word)):
    output_string.append("_")


while "_" in output_string:
    quess = str(input())
    if quess not in Secter_word:
        print('Incorrect')
    else:
        arr = findall(Secter_word, quess)
        for i in arr:
            output_string[i]=quess
        output = ""
        for i in output_string:
            output += i
        print(output)
bit_output = ""
for i in output_string:
    bit_output += i
print(bit_output)
print(True)