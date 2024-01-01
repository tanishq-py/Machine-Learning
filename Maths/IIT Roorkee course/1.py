# vector algebra
# linear combination of vector
# linear dependent and independent vectors
# orthogonal vectors
# orthonormal vectors
# feature vector

import numpy as np
x = np.array([1,0,4])
y = np.array([2,5,7])

#sum of vector
print(x+y)

#substraction of vector
print(x-y)

#sclaer multiplication
print(3*x)

#length of vector
print(np.linalg.norm(x))

#dot product
print(np.dot(x,y))
