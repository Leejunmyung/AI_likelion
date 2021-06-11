import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 14, 50)
print(type(x),x)
print(dir(x))
print(len(dir(x)))

y = np.cos(x)
y1 = np.tan(x)
plt.plot(x, y1, "r")
plt.plot(x, y)
plt.show()