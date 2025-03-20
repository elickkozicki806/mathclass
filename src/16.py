import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = x * 2 + np.random.randn(len(x))

plt.plot(x, y)
plt.show()
