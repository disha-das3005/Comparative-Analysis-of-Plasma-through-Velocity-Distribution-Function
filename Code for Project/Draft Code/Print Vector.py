import numpy as np
 
vector = np.vectorize(np.float64)
x = np.array([1, 2, 3])
x = vector(x)
print(x)
