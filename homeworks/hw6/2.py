import matplotlib.pyplot as plt
import numpy as np

x_arr =[]
y_arr =[]
for i in range(1,30):
    x_arr.append(np.random.uniform(i/50-0.05,i/50+0.05))
    y_arr.append(np.random.uniform(x_arr[i-1]+0.03,x_arr[i-1]-0.03))
x_new = np.linspace(x_arr[0],x_arr[-1],100)
y_new = np.array([y_arr[0]+(y_arr[0]-y_arr[-1])*(i-x_arr[0])/(x_arr[0]-x_arr[-1]) for i in x_new])
for i in range(len(x_arr)):
    plt.plot(x_arr[i],y_arr[i],marker="o",color = 'blue')
plt.plot(x_new,y_new,color='red')



plt.title("Best fit line using regression method")
plt.xlabel('x axis')
plt.ylabel("y axis")
plt.show()