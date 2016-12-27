import numpy as np
import matplotlib.pyplot as plt
m = 1000
n = 200

def randN1():
    return np.sqrt(-2 * np.log(np.random.uniform(0,1)))*np.cos(2*np.pi*np.random.uniform(0,1))

def randN2():
    return np.sqrt(-2 * np.log(np.random.uniform(0,1)))*np.sin(2*np.pi*np.random.uniform(0,1))

for k in range(30):
    plt.cla()
    number = 0
    resultArray = []
    for i in range(n):
        t = i / n
        for j in range(m):
            lyamda = j*np.pi
            number = number + (np.cos(lyamda*t)*randN1()+np.sin(lyamda*t)*randN2())*np.sqrt(1/(1+np.pi*j**2)**6)
        resultArray.append(number)
    plt.scatter(range(n),resultArray)
    fileName = 'grafix1/fig%d.pdf' % (k+1)
    plt.savefig(fileName)
plt.show()
