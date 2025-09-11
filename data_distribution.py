import numpy as np
from matplotlib import pyplot as plt


x = np.array(range(1,101))
print(x)
print(x[0])

y = np.random.random(100)
print(y)

z = np.random.uniform(0,1,100)
print(z)

plt.plot(z)
plt.show()

plt.hist(z,5)
plt.show()