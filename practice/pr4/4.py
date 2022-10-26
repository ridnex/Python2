class Wordplay:
    def __init__(self, arr:list):
        self.arr = arr
    
    def words_with_length(self, lenght):
        output = []
        for i in self.arr:
            if len(i)==lenght:
                output.append(i)
        return output
    
    def starts_with(self, s):
        output = []
        for i in self.arr:
            if i[0]==s:
                output.append(i)
        return output
    
    def ends_with(self, s):
        output = []
        for i in self.arr:
            if i[-1]==s:
                output.append(i)
        return output

    def palindromes(self):
        output = []
        for i in self.arr:
            if i==i[::-1]:
                output.append(i)
        return output

    def only(self, L):
        output= []
        for i in self.arr:
            str_arr = list(i)
            if str_arr.count(L) == len(i):
                output.append(i)
        return output
    
    def avoids(self, L):
        output = []
        for i in self.arr:
            if L not in i:
                output.append(i)
        return output


example = ['asx', 'trrt', 'poiiop', 'kkkk', 'lll', 'csdc']

f = Wordplay(example)

print(f.words_with_length(4))
print(f.starts_with('t'))
print(f.ends_with('c'))
print(f.palindromes())
print(f.only('k'))
print(f.avoids('l'))
