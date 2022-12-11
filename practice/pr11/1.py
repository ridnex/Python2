import re, matplotlib.pyplot as plt, numpy as np
file = open("ex1data1.txt").read().split("\n")
x, y = [], []
coordinates = {}
for line in file:
    value = list(map(float, line.split(",")))
    # print(value)
    x.append(value[0])
    y.append(value[1])
    coordinates[value[0]] = value[1]

coordinates = dict(sorted(coordinates.items(), key = lambda k: k[0]))
# print(coordinates)
# plt.plot(x, y)
# plt.plot(coordinates.keys(), coordinates.values())
# plt.scatter(coordinates.keys(), coordinates.values())
plt.scatter(x, y)
plt.show()