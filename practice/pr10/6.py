import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-10,10,10000)
y1 = np.array([(100-i*i)**(0.5)+10 for i in x1])
z1 = np.array([-(100-i*i)**(0.5)+10 for i in x1])

x2 = np.linspace(-50,50,100000)
y2 = np.array([(2500-i*i)**(0.5)+50 for i in x2])
z2 = np.array([-(2500-i*i)**(0.5)+50 for i in x2])

x3 = np.linspace(-100,100,100000)
y3 = np.array([(10000-i*i)**(0.5)+100 for i in x3])
z3 = np.array([-(10000-i*i)**(0.5)+100 for i in x3])

plt.plot(x1,y1,color = 'black')
plt.plot(x1,z1,color = 'black')

plt.plot(x2,y2,color = 'black')
plt.plot(x2,z2,color = 'black')

plt.plot(x3,y3,color = 'black')
plt.plot(x3,z3,color = 'black')

plt.grid(True)
plt.show()