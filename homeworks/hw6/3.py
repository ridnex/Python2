import math
import matplotlib.pyplot as plt
import numpy as np

x_arr = np.linspace(0,50,100)
y_arr = [math.cos(i/6) for i in x_arr]
y2_arr = [-math.cos(i/6) for i in x_arr]
y3_arr = [math.sin(i/6) for i in x_arr]
y4_arr = [-math.sin(i/6) for i in x_arr]


plt.plot(x_arr,y_arr,color = "orange")
plt.plot(x_arr,y2_arr,color = "red")
plt.plot(x_arr,y3_arr,color = "blue")
plt.plot(x_arr,y4_arr,color='green')
plt.show()