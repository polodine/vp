import numpy as np
n = 50000
print('___________________________________________')
print("Solving int(0, 1, (x^7+x^5+x^3)dx)")
b = 1
a = 0
g = 1/(b-a)
num = 0
for i in range(n):
    num = num + np.power(np.random.uniform(a,b),7)+np.power(np.random.uniform(a,b),5)+np.power(np.random.uniform(a,b),3)
print("Answer ", (1/n)*num/g)
print('___________________________________________')
print("Solving int(0, pi, (2*sin(3*x))dx)")
b = np.pi
a = 0
g = 1/(b-a)
num = 0
for i in range(n):
    num = num + 2*np.sin(3*np.random.uniform(a,b))
print("Answer ", (1/n)*num/g)
print('___________________________________________')
print("Solving int(0, Inf, (1/((x+1)*sqrt(x)))")
b = 1
a = 0
g = 1/(b-a)
num = 0
for i in range(n):
    num = num+(1/((np.random.uniform(a,b)+0.42)*np.sqrt(np.random.uniform(a,b))))
I = (1/n)*num/g

b =100
a = 1
g = 1/(b-a)
num = 0
for i in range(n):
    num = num+(1/((np.random.uniform(a,b)+1)*np.sqrt(np.random.uniform(a,b))))

I = I + (1/n) * num/g

b = 100000000
a = 100
g = 1/(b-a)
num = 0
for i in range(n):
    num = num+(1/((np.random.uniform(a,b)+1)*np.sqrt(np.random.uniform(a,b))))

I = I+(1/n)*num/g
print("Answer ", I)