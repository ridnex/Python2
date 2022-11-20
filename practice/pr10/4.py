import math
import random
import numpy.random
import matplotlib.pyplot as plt

alpha = numpy.random.randint(0, 100, 80) 

x1 = numpy.random.randint(0, 120, 80)
y1 = numpy.random.randint(0, 120, 80)
area = numpy.random.randint(0, 120, 80)
colors = numpy.random.randint(1, 30, 80)
areas = [int(i**2*math.pi)/100 for i in area ]

plt.figure()
plt.scatter(x1/100, y1/100, s=areas, c=colors, alpha=alpha/100)
plt.axis([-0.2, 1.2, -0.2, 1.2])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()