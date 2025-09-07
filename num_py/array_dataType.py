import numpy as np

a = np.array([1.1,2.1,3.1,4.1,5.1])
print(type(a))
print(type(a[0]))

b = a.astype(int)
print(type(b))
print(b)

c = a.astype(bool)
print(type(c))
print(c)