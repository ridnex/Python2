import math
import numpy.random
import matplotlib.pyplot as plt


x1 = numpy.random.randint(0, 60, 100)
y1 = numpy.random.randint(0, 8000, 100)

x2 = numpy.random.randint(0, 80, 100)
y2 = numpy.random.randint(0, 8000, 100)


x3 = numpy.random.randint(45, 85, 100)
y3 = numpy.random.randint(0, 8000, 100)

x4 = numpy.random.randint(20, 80, 100)
y4 = numpy.random.randint(0, 8000, 100)


plt.figure()

plt.xlabel('x label')
plt.ylabel('y label')

plt.subplot(221)
plt.scatter(x1/100, y1, color = 'green')
plt.title("Spring", color = "green")
plt.xlim(0, 0.6)
plt.ylim(0, 8000)

plt.subplot(222)
plt.scatter(x2/100, y2, color = 'yellow')
plt.title("Summer", color = 'yellow')
plt.xlim(0, 0.8)
plt.ylim(0, 8000)


plt.subplot(223)
plt.scatter(x3/100, y3, color = 'red')

plt.title("Autumn", color = 'red')
plt.xlim(0.45, 0.85)
plt.ylim(0, 9000)

plt.subplot(224)
plt.scatter(x4/100, y4, color = 'blue')
plt.title("Winter", color = 'blue')
plt.xlim(0.2, 0.8,0.1)
plt.ylim(0, 8000, 2000)

plt.legend()

plt.show()
