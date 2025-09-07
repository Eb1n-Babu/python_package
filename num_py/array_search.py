import numpy as np

a = np.arange(24)
c = np.searchsorted(a,3)
print(c)

b = np.arange(24,48,1)
e = np.searchsorted(b,29)
print(e)