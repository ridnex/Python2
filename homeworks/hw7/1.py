import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as lag
import math

x = int(input("number: "))

print("Number's square: ", x**2)
print("Number's cube: ",   x**3)

theta = float(input("angle θ : "))

type = input("Write Radians or Degrees: ")

if type == 'Radians':
    print(math.cos(theta),math.sin(theta))
else:
    print(math.cos(math.radians(theta)),math.sin(math.radians(theta)))

meshpoints = np.linspace(-1,1,500)
print("53th element of meshPoints: ", meshpoints[52])

plt.plot(meshpoints,(np.sin(2*math.pi*meshpoints)))
plt.savefig("1picture")
plt.show()