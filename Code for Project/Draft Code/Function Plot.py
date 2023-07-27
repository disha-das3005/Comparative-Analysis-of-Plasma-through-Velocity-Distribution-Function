import numpy as np
import matplotlib.pyplot as plt

def f(x):                      #defining function
    return x**2*np.exp(-x**2)
x = np.linspace ( start = 0.    # lower limit
                , stop = 3      # upper limit
                , num = 51      # generate 51 points between 0 and 3
                )
y = f(x)    # This is already vectorized, that is, y will be a vector!
plt.plot(x, y)
plt.show()
