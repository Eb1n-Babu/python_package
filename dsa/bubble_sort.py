from random import random

from matplotlib import pyplot as plt

y = []

for k in range(10):
    x = int(random()*100)
    y.append(x)

print(y)


for i in range(len(y)+1):
    for j in range(len(y)-1):
        if y[j] > y[j+1]:
            y[j], y[j+1] = y[j+1], y[j]
            plt.plot(y)
            plt.show()
            plt.close()
print(y)



