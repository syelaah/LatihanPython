import numpy as np

a = np.array(([1,2,3],
              [4,5,6],
              [7,8,9]))

b=np.ones([3,3])

print("matriks a:")
print(a)

print("matriks b:")
print(b)

c = np.dot(a,b)
print("matriks c:")
print(c)

