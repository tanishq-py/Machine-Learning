# types of matrix
# matrix algebra
# matrix multilplication - no of column of A = no of rows of B
# transpose of matrix
# determinant of matrix
# inverse of matrix - if det=0, inverse not exist. 
# a.a-1=I

import numpy as np
p = np.array([[1,7],[2,3],[2,4]])
q= np.array([[2,0],[4,8],[2,7]])
print(p+q)
print(p-q)

#define 2,3 matrix
r= np.array([[1,6,3],[2,6,10]])

#matrix multplication
t= np.dot(p,r)
print(t)

#determinant
print(np.linalg.det(t))

#inverse
print(np.linalg.inv(q))
