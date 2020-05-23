import matplotlib.pyplot as plot
import numpy as np

x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
plot.plot(x,y)
plot.show()