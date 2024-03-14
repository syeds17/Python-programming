"""A Simple Graph"""          #For better output use Python 3.12.1 (IDLE) Shell or JUPITER NoteBook....

import mathplotlib.pyplot as plt   #Importing modules
import numpy as np

x = np.linspace(0,2,100)

plt.plot(x,x,label="linear")
plt.plot(x,x**2,label="quadratic")   #ploting the curves
plt.plot(x,x**3,label="cubic")

plt.xlabel("x-label")
plt.ylabel("y-label")
plt.title("Simple plot")   #labeling graph
plt.legend()
plt.show()

