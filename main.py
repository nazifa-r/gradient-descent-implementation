import numpy as np
import matplotlib.pyplot as plt

#our goal is to find x that makes y as small as possible
def y_function(x):
    return x**2

def y_derivative(x):
    return 2*x;

x = np.arange(-100, 100, 0.1) #creating the dataset
y = y_function(x)

curr_pos = (80, y_function(80))
learning_rate = 0.01 #higher the learning rate, faster we converge
#learning rate of 1 oscillates but it doesn't diverge

for _ in range(1000):


    x_new = curr_pos[0] - (learning_rate * y_derivative(curr_pos[0]))
    y_new = y_function(x_new)
    curr_pos = (x_new, y_new)
    plt.plot(x,y)
    plt.scatter(curr_pos[0], curr_pos[1], color="red")
    plt.pause(0.001)
    plt.clf()
    #plt.show()



