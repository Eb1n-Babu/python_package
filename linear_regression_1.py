from matplotlib import pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

def my_func(i):
    return slope * i + intercept

my_model = list(map(my_func, x))

print(r_value)

plt.scatter(x, y)
plt.plot(x, my_model)
plt.show()