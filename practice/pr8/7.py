import numpy 

class Sudoku():
    def __init__(self, str1):
        self.str1 = str1
        
    
    def board(self):
        self.out = []
        list_part_str = ''
        for i in range(len(self.str1)):
            list_part_str += self.str1[i]
            if i%9==8:
                self.out.append(list(list_part_str))
                list_part_str = ''
        
        self.array = numpy.array(self.out)
        return self.array


    def get_row(self, n): 
        return self.array[n]

    def get_column(self, n):
        return self.array[:, n]

    def get_sqr(self, arr:list):
        if len(arr)==1:
            n = arr[0]
        
            row = (n//3)*3
            column = (n%3)*3
            out = []
            for i in range(row, row+3):
                for j in range(column, column+3):
                    out.append(self.array[i][j])
            return out
            
        else:
            i, j = arr[0], arr[-1]
            n = (i//3)*3+(j//3)
            
            row = (n//3)*3
            column = (n%3)*3
            out = []
            for i in range(row, row+3):
                for j in range(column, column+3):
                    out.append(self.array[i][j])
            return out

Sd = Sudoku('417950030000000700060007000050009106800600000000003400900005000000430000200701580')
print(Sd.board())
print(Sd.get_row(2))
print(Sd.get_column(3))
print(Sd.get_sqr([1]))
print(Sd.get_sqr([1, 8]))
print(Sd.get_sqr([8, 3]))