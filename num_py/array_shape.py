import numpy as np

a = np.array(range(18))
print(a)
b = a.reshape(2,3,3)
c = a.reshape(3,6)

print(a.shape)
print(b.shape)
print(c.shape)