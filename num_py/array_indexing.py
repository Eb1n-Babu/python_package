import numpy as np

a = np.array(range(10))
print(a)

print(a[0])
print(a[-1])
print(a[3]+a[5])

b = a.reshape(2,5)
print(b)

c = np.array(range(18))
f = c.reshape(2,3,3)
print(f)