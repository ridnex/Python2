import matplotlib.pyplot as plt
import numpy as np

x_arr = []
y_arr = []
for i in range(0,1000,20):

    x_arr.append(np.random.randint(i,i+2))
    y_arr.append(np.random.randint(5,90))

plt.plot(x_arr,y_arr,marker="^",color="blue")
plt.title("This is the title")
plt.xlabel('This is the X axis')
plt.ylabel('This is the Y axis')
plt.legend('curve',loc = "upper right")
plt.show()