from matplotlib import pyplot as plt

x = list(range(10))
y = list(range(11,21,1))

plt.plot(x,y,drawstyle='steps-post')
plt.show()
