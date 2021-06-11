import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0,14,50)
y1 = np.sin(x1)

x2 = np.linspace(0,14,50)
y2 = np.cos(x2)

x3 = np.linspace(0,14,50)
y3 = np.tan(x3)

plt.figure(figsize=(16,8))
plt.plot(x1,y1,'r',label="sin")
plt.plot(x2,y2,'g',label="cos")
plt.plot(x3,y3,'b',label="tan")
plt.legend()
plt.title('graph plot')
plt.show()