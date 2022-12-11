import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
from math import *

vec1 = np.array([ -1., 4., -9.])
mat1 = np.array([[ 1., 3., 5.], [7., -9., 2.], [4., 6., 8. ]])
vec2 = np.pi/4*vec1
print(vec2)
vec2 = np.cos(vec2)
print(vec2)
vec3 = vec1 + 2*vec2
print(vec3)
length = la.norm(vec3)
print(length)
vec4= mat1.dot(vec3)
print(vec4)
mat2 = mat1.T
print(mat2)
det = la.det(mat1)
print("det:", det)
trace = sum(np.diag(mat1))
print('trace:', trace)

min_element = np.min(vec1)
print("min_in_vector", min_element)
coeff, = np.where(np.isclose(vec1, min_element))
print("j in vector[j]=min", coeff)

min_element_in_matrix = np.min(mat1)
print('min_element_in_matrix', min_element_in_matrix)
i,j = np.where(np.isclose(mat1, min_element_in_matrix))
print("i and j of min", i, j)


A=np.array([[17, 24, 1, 8, 15],
[23, 5, 7, 14, 16],
[ 4, 6, 13, 20, 22],
[10, 12, 19, 21, 3],
[11, 18, 25, 2, 9]])

B = A.T

sum_row = np.array([sum(A[0]),sum(A[1]),sum(A[2]),sum(A[3]),sum(A[4])])
sum_column = np.array([sum(B[0]),sum(B[1]),sum(B[2]),sum(B[3]),sum(B[4])])
sum_d1=sum(np.diag(A))
sum_d2 =sum(np.diag(np.fliplr(A)))
arr = np.array([sum_d1,sum_d2,np.min(sum_row),np.max(sum_row),np.min(sum_column),np.max(sum_column)])
for i in arr:
    print(i)
if np.min(arr)==np.max(arr):
    print("yes")
else:
    print("No")





M = np.array([np.random.rand(10) for i in range(10)])
print(M)

MUL = M[:5, :5]
MUR = M[5:10, :5]
MLL = M[:5, 5:10]
MLR = M[5:10, 5:10]
print(MUL)
print(MUR)
print(MLL)
print(MLR)