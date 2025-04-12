import matplotlib.pyplot as plt
import numpy as np
import os

# Plotting a List
new_data = np.arange(9)
plt.plot(new_data)
plt.title("New Data Line"); plt.xlabel("X values"); plt.ylabel("Y Values")
plt.show()

# Plotting 2 Lists
x = [1 ,2, 3, 4, 5, 6, 7]
y = [1, 4, 9, 16, 25, 36, 49]
plt.plot(x,y)
plt.title("New Data Line"); plt.xlabel("X values"); plt.ylabel("Y Values")
plt.show()

# Plotting Multiple data sets
data = np.arange(2, 7, 0.3)
#   plot(x1,  y1,  shape/color1, x2, y2, shape/color2, x3, y3, shape/color 3  )
plt.plot(data, data, "r--", data, data**2, "bs", data, data**3, "g^")
plt.title("Data ^1, ^2, and ^3"); plt.xlabel("X values"); plt.ylabel("Y Values")
plt.show()

# save last graph to png file in correct folder
og_dir = os.getcwd()
os.chdir("Data Visualization Files")
plt.savefig("numbers_squared_and_cubed.png")
os.chdir(og_dir)

# Create bar graphs
films = ["film1", "film2", "film3"]
awards = [3, 7, 4]
plt.bar(films, awards)
plt.title("Films By Awards"); plt.xlabel("Films"); plt.ylabel("No. of Awards")
plt.show()

# Create histogram
new_h = np.random.normal(150, 15, 230)
plt.hist(new_h)
plt.show()

# Creating Pie Charts
parts = np.array([35, 25, 25, 15])
ch_labels = ["first", "second", "third", "fourth"]
myexplode = [0.2, 0, 0, 0]
plt.pie(parts, labels= ch_labels, explode = myexplode, autopct= '%.1f' , shadow = True)
plt.legend(title = "Groups:", loc="upper left")
plt.show()