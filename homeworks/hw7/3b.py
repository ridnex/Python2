import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

def r(r0, angle):
    return r0 + np.cos(angle)

def x(r, angle):
    return r*np.cos(angle)

def y(r, angle):
    return r*np.sin(angle)

angle_arr = np.arange(0, 2*np.pi, 0.01)
r1 = 0.8
r2 = 1.0
r3 = 1.2
x1, x2, x3, y1,y2, y3  = [], [], [], [], [], []

for i in range(len(angle_arr)):
    x1.append(x(r(r1, angle_arr[i]), angle_arr[i]))
    x2.append(x(r(r2, angle_arr[i]), angle_arr[i]))
    x3.append(x(r(r3, angle_arr[i]), angle_arr[i]))
    y1.append(y(r(r1, angle_arr[i]), angle_arr[i]))
    y2.append(y(r(r2, angle_arr[i]), angle_arr[i]))
    y3.append(y(r(r3, angle_arr[i]), angle_arr[i]))
   
ax1.plot(x1, y1)
ax2.plot(x2, y2)
ax3.plot(x3, y3)


plt.savefig("3b.pdf")
plt.show()