import numpy as np
v= np.array([[1,2,1],[3,2,4],[1,-1,1]])
print(v)

#calculate eignepairs
values, vectors = np.linalg.eig(v)
print(values)
print(vectors)
