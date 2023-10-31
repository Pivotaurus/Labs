import matplotlib.pyplot as plt
import numpy as np

radius = 1.0

center = (0, 0)

angles = np.linspace(0, 2 * np.pi, 6)

x = center[0] + radius * np.cos(angles)
y = center[1] + radius * np.sin(angles)

plt.fill(x, y, 'red')

plt.title('Правильный пятиугольник')
plt.axis('equal')

plt.show()
