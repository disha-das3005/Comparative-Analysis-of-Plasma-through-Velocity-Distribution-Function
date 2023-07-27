# importing the required module
import matplotlib.pyplot as plt
  
# x axis values
x = [0.43, 0.62, 0.23, 0.7, 0.31, 0.04, 0.27, 0.43, 0.71, 0.46]
# corresponding y axis values
y = [0.078328,0.077636,0.078907,0.077345,0.078704,0.079177,0.078811,0.0783280,0.077310,0.078223]
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('cold plasma graph!')
  
# function to show the plot
plt.show()
