from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X_arr = np.linspace(-2,16,100)
x = [math.cos(i) for i in X_arr]
y = [math.sin(i) for i in X_arr]
z = [10*i for i in X_arr]
ax.plot(x,y,z,zdir='z',label='zs=0, zdir=z',marker = 'o')
ax.view_init(30,45)
plt.show()