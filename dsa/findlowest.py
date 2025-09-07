from matplotlib import pyplot as plt

a = list(range(100,21,-1))
print(a)
b = sorted(a)
print(b[0])

plt.plot(a)
plt.show()

