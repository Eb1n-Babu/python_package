import numpy as np

a  = np.arange(24,48,1)
print(a)

b = np.arange(48,24,-1)
print(b)

c = b.sort()

print(sorted(b))
print(c)