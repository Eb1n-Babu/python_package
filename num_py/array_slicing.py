import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(a[1:5:2])
print(a[1:5])
print(a[::2])

b = a.reshape(3,5)
print(b)
print(b.shape)
print(b.ndim)

print(b)
print("=")
print(b[0:3 , 1:3])