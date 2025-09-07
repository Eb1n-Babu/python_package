import numpy as np

a = np.array(range(18))
print(a)

b = np.copy(a)
print(b)

c = a.copy()
print(c)
d = c.view()
c[0] = 45

print(c)
print(d)


