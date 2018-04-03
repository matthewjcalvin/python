import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x0 = 0
y0 = 1
xf = 10
n = 101
delta = (xf -x0)/(n-1)
x = np.linspace(x0,xf,n)
y = np.zeros([n])
y[0] = y0
for i in range(1,n):
    y[i] = delta*(-y[i-1] +np.sin(x[i-1])) + y[i-1]
for i in range(n):
    print(x[i],y[i])
plt.plot(x,y, '-')
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Approximate Solution with Forward Euler's Method")
plt.show()
