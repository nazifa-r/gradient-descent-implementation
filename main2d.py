import numpy as np
import matplotlib.pyplot as plt

# our goal is to find x, y that makes z as small as possible
def z_function(x, y):
    return x**2 + 5* (y**2)

def dx(x):
    return 2*x

def dy(y):
    return 10*y

x = np.arange(-10, 10, 0.2)
y = np.arange(-10, 10, 0.2)
X, Y = np.meshgrid(x, y) # all x and y coordinates arranged in grid format
Z = z_function(X, Y)

curr_pos = (8, 8)
learning_rate = 0.1


path_x = [] # all x positions over time
path_y = [] # all y positions over time

for _ in range(100):

    x_new = curr_pos[0] - learning_rate * dx(curr_pos[0])
    y_new = curr_pos[1] - learning_rate * dy(curr_pos[1])

    curr_pos = (x_new, y_new)

    path_x.append(curr_pos[0]) # keep adding current position to form a trail/path
    path_y.append(curr_pos[1])

    # heatmap background
    plt.contourf(X, Y, Z, levels=50, cmap="viridis") # color style blue -> green -> yellow
    plt.contour(X, Y, Z, levels=30, colors="black", alpha=0.3) # draw lines on top of the colored map

    # path + current position
    plt.plot(path_x, path_y, color="white", linewidth=2) # to draw the path
    plt.scatter(curr_pos[0], curr_pos[1], color="red")

    plt.pause(0.1)
    plt.clf()

plt.show()