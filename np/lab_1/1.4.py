import numpy as np
import math as mat

alpha1 = np.random.uniform(0, 1, 1)
alpha2 = np.random.uniform(0, 1, 1)
eta1 = mat.sqrt(-2 * mat.log(alpha1))*mat.cos(2 * mat.pi * alpha2)
eta2 = mat.sqrt(-2 * mat.log(alpha1))*mat.sin(2 * mat.pi * alpha2)
print(eta1)
print(eta2)
n = 5
num = 0
for i in range(n):
    num = num + np.random.uniform(0, 1)
print(mat.sqrt(12/n) * (num - n/2))
