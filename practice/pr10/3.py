import matplotlib.pyplot as plt
import numpy as np
import numpy.random


x1 = numpy.random.randint(0, 30, 30)
y1 = numpy.random.randint(0, 30, 30)

x2 = numpy.random.randint(40, 70, 30)
y2 = numpy.random.randint(0, 50, 30)


x3 = numpy.random.randint(60, 120, 30)
y3 = numpy.random.randint(0, 100, 30)
plt.figure()

plt.scatter(x1/100, y1/100, label ='water' , color = "blue")
plt.scatter(x2/100, y2/100, label ='tea', color = "green")
plt.scatter(x3/100, y3/100, label ='coffee', color = "red")

plt.axis([-0.2, 1.4, -0.2, 1.2])
plt.legend(loc = 'upper left')

plt.xlabel("X")
plt.ylabel("Y")
plt.show()