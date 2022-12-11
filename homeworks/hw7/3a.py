import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.e**(-x/10)*np.sin(np.pi*x)
g = lambda x: x*np.e**(-x/3)

x = np.arange(0, 10.5, 0.5)
x0 = np.linspace(0,10,1000)

y_f = f(x0)
y_g = g(x0)

plt.plot(x0, y_f, label = "f(x)", color = "blue")
plt.plot(x0, y_g, label = "g(x)", color = "red")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0, 10)
plt.legend()
plt.savefig("3py.jpg")
plt.show()