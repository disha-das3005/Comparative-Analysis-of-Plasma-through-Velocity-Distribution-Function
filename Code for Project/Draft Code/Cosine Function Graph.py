import numpy as np
import matplotlib.pyplot as plt
 
in_array = np.linspace(-(2*np.pi), 2*np.pi, 20)
out_array = np.cos(in_array)
 
print("in_array : ", in_array)
print("\nout_array : ", out_array)
 
# red for numpy.cos()
plt.plot(in_array, out_array, color = 'red', marker = "o")
plt.title("numpy.cos()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
