import numpy as np

a = np.arange(24,48,1).reshape(6, 4)
b = np.arange(0,24,1).reshape(6, 4)

print(a)
print(b)

c = np.concatenate((a, b), axis=0)
print(c)

d = np.array([1,2,3,4,5])
r = np.array([1,2,3,4,5])

f = np.concatenate((d, r), axis=0)
print(f)