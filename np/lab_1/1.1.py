import numpy as np
import random
import math
import matplotlib.pyplot as plt

y = np.random.uniform(0,1,1000000)

plt.hist(y, 100)
plt.show()

L = []
n = 1000

for i in range(n):
    L.append(random.random())

k = round(2*math.log(n))
MAX = L[0]
pos = 0
for i in range (len(L)):
    if L[i]>MAX: MAX = L[i]; pos = i

MIN = MAX
pos = 0
for i in range (len(L)):
    if L[i]<MIN: MIN = L[i]; pos = i

R = MAX - MIN
dx = R/k
Range = []

for i in range (k):
    Range.append (MIN + (i+1)*dx)
Chastota = []

for i in range (k):
    entries = 0
    for j in range(n):
        if (L[j] >= (Range[i] - dx) and L[j] < Range[i]):
            entries = entries + 1
    Chastota.append (entries)


P = []
j = 0
M = 0
for j in range (k):
     P.append (Chastota[j]/n)
     M = M + P[j]

j = 0
chi2 = 0
for j in range(k):
        adder = ((P[j] - (1/n))**2)/P[j]
        chi2 = chi2 + adder

print ("Хи квадрат спостережуване = ", chi2)