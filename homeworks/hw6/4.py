import matplotlib.pyplot as plt

countries = ["India","UK","US", "South Korea","Australia",   "Germany"]
density = [27.7,24.6,18.5, 9.2, 3.4,16.5]
explode = [0,0,0.2,0,0,0]
colors_for_pie = ['red', 'green', 'blue','yellow','purple','orange']
plt.pie(density,explode,labels = countries, colors = colors_for_pie,  shadow=True, startangle=150, autopct='%1.1f%%')
plt.title("Population Density Index")
plt.show()