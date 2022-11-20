import matplotlib.pyplot as plt
import numpy as np

divisions = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
avarage = [25, 48, 75, 10, 16, 67, 30]
colors=['blue', 'green', 'yellow', 'orange', 'purple', 'red', 'brown']
plt.bar(divisions, avarage, color=colors)
plt.show()



