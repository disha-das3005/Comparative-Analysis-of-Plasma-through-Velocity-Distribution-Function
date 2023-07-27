
# importing the required module
import matplotlib.pyplot as plt
  
# x axis values
x = [0.43, 0.62, 0.23, 0.7, 0.31, 0.04, 0.27, 0.43, 0.71, 0.46]
# corresponding y axis values
y = [0.112037,0.107716,0.116365,0.106094,0.114755,0.118716,0.115590,0.112037,0.105904,0.111336]
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('Hot plasma graph!')
  
# function to show the plot
plt.show()
