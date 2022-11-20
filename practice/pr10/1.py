import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1, 1, 100)

plt.plot(x, x**2, label='quadratic', color = 'black')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("X**2")
plt.legend()
plt.show()