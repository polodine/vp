import matplotlib.pyplot as plt
import numpy as np

n = 10000  # кількість елементів масиву
k = 1000   # кількість масивів
m = 100    # кількість стовбців в гістаграмі

max = []   # випадкова величина

for i in range(n):
    y = np.random.uniform(0, 1, k)
    max.append(np.amax(y))

plt.hist(max, m)
plt.show()
