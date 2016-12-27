import matplotlib.pyplot as plt
import numpy as np
import math as mat

n = 10000
m = 25
l = 40
SQR = mat.sqrt(12 / n)
result = []  # результуючий масив

# 1
for i in range(n):
    result.append(mat.sqrt(-2 * mat.log(np.random.uniform(0, 1, 1)))*mat.cos(2 * mat.pi * np.random.uniform(0, 1, 1)))

plt.hist(result, m)
plt.show()
result.clear()

# 2
for i in range(n):
    result.append(mat.sqrt(-2 * mat.log(np.random.uniform(0, 1, 1)))*mat.sin(2 * mat.pi * np.random.uniform(0, 1, 1)))

plt.hist(result, m)
plt.show()
result.clear()

# 3
for i in range(n):
    num = 0
    for j in range(l):
        num = num + np.random.uniform(0, 1)
    result.append(SQR * (num - l/2))

plt.hist(result, m)
plt.show()

