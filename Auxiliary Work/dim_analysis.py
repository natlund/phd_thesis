import numpy as np

# Dimensional Matrix
M = np.array([[1,-3, 1,-1,-1,1],[0,1,0,1,1,0],[0,0,-1,1,-2,0]])

print M

I = np.identity(6)

T = np.concatenate([M,I])

A = T.transpose()

print I
print T
print A

