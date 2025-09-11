import numpy as np
from scipy import stats

data = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean_value = np.mean(data)
print(mean_value)

median_value = np.median(data)
print(median_value)

mode_value = stats.mode(data)
print(mode_value)

data_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
x = np.mean(data_1)
y = np.median(data_1)
z = stats.mode(data_1)
print(x)
print(y)
print(z)