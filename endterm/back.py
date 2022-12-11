import numpy as np

# matrix = np.array([ 

#   [3, 2, 0],  

#   [0, 1, 2], 

#   [0, 3, 1]

# ] )

# matrix = np.array([ 

#   [3, 0, 0],  

#   [0, 1, 4], 

#   [0, 2, 2]

# ] )
matrix = np.array([ 

  [1, 0, 0],  

  [0, 2, 0], 

  [0, 0, 3]

] )


mod1=5

def smaller_matrix(original_matrix, column):
    for ii in range(len(original_matrix)):
        new_matrix=np.delete(original_matrix,ii,0)
        new_matrix=np.delete(new_matrix,column,1)
        return new_matrix

def determinant(matrix:list):
    r = len(matrix)
    if r==2:
        simple_determinant = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        return simple_determinant
    else: 
        answer=0
        for j in range(r):
            cofactor = (-1)**(0+j) * matrix[0][j] * determinant(smaller_matrix(matrix,j))
            answer+= cofactor
        return answer

def square_matrix(matrix, mod):
    
    new_matrix = np.dot(np.transpose(matrix), matrix)
    for i in range(len(new_matrix)):
        for j in range((len(new_matrix))):
            new_matrix[i][j] = new_matrix[i][j]%mod
    
    return new_matrix


square1 = square_matrix(matrix, mod1)

# square2=  square_matrix(matrix2, mod1)

def A_minus_iegenI(matrix, value, mod):
    
    null = matrix.copy()
    for i in range(len(matrix)):    
        null[i][i]=(matrix[i][i]-value)%mod
    return null

def evalue_first_order(matrix, mod):
    e_value=[]
    for i in range(mod):
        if determinant(A_minus_iegenI(matrix, i, mod))%mod==0:
            e_value.append(i)
    return e_value

def char_pol_for_3(matrix, mod):
    coeff = np.array([1,((-1)*sum(np.diag(matrix)))%mod])
    summ = 0
    for i in range(3):
        new_matrix = np.array([])
        joined = np.concatenate((matrix[0:i],matrix[i+1:]))
        for j in range(2):
            new_matrix = np.append(new_matrix,np.concatenate((joined[j][0:i],joined[j][i+1:])))
        new_matrix = new_matrix.reshape(2,2)
        summ+=determinant(new_matrix)
    coeff = np.append(coeff,summ%mod)
    coeff = np.append(coeff,((-1)*determinant(matrix))%mod)
    return coeff

def ghorner(pol,root):
    rem = np.array([pol[0]])
    for i in range(0,len(pol)-1):
        rem = np.append(rem,(root*rem[i]+pol[i+1])%5)
    return rem[:-1]


def evalu_all(matrix, mod):
    eign = evalue_first_order(matrix, mod)
    if len(eign)==0:
        print("Not evalue in Z5")
        return False
    else:
        upgrade = [eign[0]]
        chrpol = char_pol_for_3(matrix, mod)
        pol = ghorner(chrpol,eign[0])
        for i in range(mod):
            point = (i**2)+pol[1]*i+pol[2]
            if point%mod==0:
                upgrade.append(i)
            point = 0
        if len(upgrade)==1:
            return [upgrade[0],upgrade[0],upgrade[0]]
        elif len(upgrade)==2:
            return [upgrade[0],upgrade[1],upgrade[1]]
        else:
            return upgrade

def RREF(matrix, mod):
    identity = np.diagflat([1 for i in range(len(matrix))])
    if mod==5:
        inverses = {1:1,2:3,3:2,4:4,0:1}
    elif mod ==7:
        inverses = {1:1,2:4,3:5,4:2,5:3,6:6, 0:1}
    elif mod ==3:
        inverses = {1:1,2:2,0:1}
    elif mod ==2:
        inverses = {1:1,0:1}

    if matrix[0][0]==0:
        matrix = matrix[::-1]
        identity = identity[::-1]
    rows = np.shape(matrix)[0]
    columns = np.shape(matrix)[1]
    for i in range(columns-1):
        for j in range(i+1,rows):
            pls1,pls2 = np.array([num%mod for num in matrix[j,:]]),np.array([num%mod for num in identity[j,:]])
            mns1,mns2 = np.array([num%mod for num in matrix[i,:]]),np.array([num%mod for num in identity[i,:]])
            prdct = (matrix[j][i]*inverses[(matrix[i][i])%mod])%mod
            matrix[j,:] = (pls1-prdct*mns1)%mod
            identity[j,:] = (pls2-prdct*mns2)%mod
    if (matrix[1]==matrix[2]).all():
        matrix[2]=(matrix[2]-matrix[1])%mod
        identity[2]=(identity[2]-identity[1])%mod
    if (matrix[0]==matrix[1]).all():
        matrix[1]=(matrix[1]-matrix[0])%mod
        identity[1]=(identity[1]-identity[0])%mod
    if (matrix[0]==matrix[2]).all():
        matrix[2]=(matrix[2]-matrix[0])%mod
        identity[2]=(identity[2]-identity[0])%mod
    return [matrix,identity]
   

def cef(matrix):
    column_matrix = matrix.T
    arr = RREF(column_matrix, mod1)
    x,y = arr[0].T,arr[1].T
    return [x,y]

def eigenvector(matrix,value):
    new_matrix = matrix-np.diagflat([value for i in range(len(matrix))])
    dta = cef(new_matrix)
    x,y = dta[0].T,dta[1].T
    output = []
    for i in range(len(x)):
        cnt = 0
        for j in range(len(x)):
            if x[i][j]==0:
                cnt+=1
        if cnt==3:
            output.append(y[i])
    return output
def mod_5(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            array[i][j]= array[i][j]%5
    return array
def overall(matrix, mod):
    uniq_evalue = evalue_first_order(matrix, mod)
    #print("UNIQ", uniq_evalue)
    e_values = evalu_all(matrix, mod)
    e_vectors = []
    for i in uniq_evalue:
        out = eigenvector(matrix, i)
        if len(out)>1:
            new_1 = gs_for_vec(out)
            new_out = normalized(new_1)
        else:
            new_out = normalized(out)
        for j in new_out:
            e_vectors.append(j)
    if len(e_values)!=len(e_vectors):
        print('SVD in Z5 does not exist')
        return False
    return e_vectors


def gs_cofficient(v1, v2):
    return ((np.dot(v2, v1))/ (np.dot(v1, v1)))
    
def mod_5(u2):
    for i in range(len(u2)):
        u2[i]=u2[i]%5
    return u2

def gs_for_vec(X):
    if len(X)==2:
        u1 = X[0]
        coef = gs_cofficient(u1, X[1])
        new_vect = np.dot(coef,u1)
        u2 = np.subtract(X[1], new_vect)
        
        Y=[mod_5(u1), mod_5(u2)]

        return Y
    elif len(X)==3:
        u1 = X[0]
        coef = gs_cofficient(u1, X[1])
        new_vect = np.dot(coef,u1)
        u2 = np.subtract(X[1], new_vect)
        coef1 = gs_cofficient(u1, X[-1])
        coef2 = gs_cofficient(u2, X[-1])
        new_vect_1 = np.dot(coef1,u1)
        new_vect_2 = np.dot(coef2, u2)
        new_new = np.subtract(X[-1], new_vect_1)
        u3 = np.subtract(new_new, new_vect_2)

        Y=[mod_5(u1), mod_5(u2), mod_5(u3)]
        return Y

# def compare(H, mode=0):
#     # The tolerance for comparison purposes
#     tol = 1e-12

#     # Select function depending upon the value of mode
#     if mode == 0:
#         res = eig_sq(H)
#     elif mode == 1:
#         res = eig_sq_perf(H)
#     elif mode == 2:
#         res = eig_sq_vect(H)
#     else:
#         raise IndexError

#     # Return the comparison matrix
#     return abs(res - eig_sq_np(H)) < tol

   
import math
def new_round(n):
    eps = 0.001
    if abs(round(n) - n) < eps: return round(n)
    else: return n

def normalized(X): 
    P = []
    for column_vec in X:
        out = []
        cnt = 0
        for j in range(len(column_vec)):
            cnt+= column_vec[j]**2
        k = math.sqrt(cnt)
        for j in range(len(column_vec)):
            out.append(new_round(column_vec[j]/k))
        P.append(out)
        Z = np.array(P)
    return Z

def diogonal(matrix):
    e_values = evalu_all(matrix, 5)
    n = len(matrix)
    X = []
    for i in range(n):
        out = []
        for j in range(n):
            if i == j:
                out.append(math.sqrt(e_values[i]))
            else:
                out.append(0)
        X.append(out)
    Y = np.array(X)
    return Y

def inverse_diogonal(matrix):
    e_values = evalu_all(matrix, 5)
    n = len(matrix)
    X = []
    for i in range(n):
        out = []
        for j in range(n):
            if i == j:
                if e_values[i]!=0:
                    out.append(1/math.sqrt(e_values[i]))
                else:
                    out.append(0)
            else:
                out.append(0)
        X.append(out)
    Y = np.array(X)
    return Y



Matrix_V = np.array(overall(square1, 5))

Matrix_VV = np.transpose(Matrix_V)

Matrix_D = np.array(diogonal(square1))

Matrix_DD = np.array(inverse_diogonal(square1))

Matrix_AVV = np.matmul(matrix, Matrix_VV)
Matrix_B = np.matmul(Matrix_AVV, Matrix_DD)


Matrix_BD = np.matmul(Matrix_B, Matrix_D)
Matrix_BDV = np.matmul(Matrix_BD, Matrix_V)

txt_ans = ''
txt_ans += f" matrix B:\n {Matrix_B}\n\n"
txt_ans += f" matrix D:\n {Matrix_D}\n\n"
txt_ans += f" matrix V:\n {Matrix_V}\n\n"
print(txt_ans)
print(square1)
print("UNIQ Evalues:", evalue_first_order(square1, 5))
print("ALL Evalues", evalu_all(square1, 5))
print('evectors')
for i in overall(square1, 5):
    print(i)
# print(Matrix_B)
# print(Matrix_D)
# print(Matrix_V)