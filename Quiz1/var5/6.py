anagram = 'asd'
string = 'bhbhbhdsabhbhbhb'
arr = list(string)
indexes = []

# i want to assume that this letters from anagram dont have dublicates

for i in anagram:
    indexes.append(arr.index(i))

def correct(array : list)->bool:
    for i in range(len(array)):
        if i!=len(array) -1 and array[i+1]-array[i]!=1:
            return False
    return True



indexes.sort()
print(correct(indexes))