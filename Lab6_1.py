#1)	Построить график функции y=2/(x-5). 
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2/(x-5)

x = np.linspace(-10, 10, 100)

y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y=2/(x-5)')
plt.grid(True)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.show()