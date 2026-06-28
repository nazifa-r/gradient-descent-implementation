import numpy as np 
import matplotlib.pyplot as plt

def z_function(x, y):
    return (np.sin(5*x) * np.cos(5*y)) / 5

def calculate_gradient(x, y):
    return np.cos(5*x) * np.cos(5*y), - np.sin(5*x) * np.sin(5*y)

x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

curr_pos = (0.7, 0.4, z_function(0.7, 0.4))
learning_rate = 0.1

ax = plt.subplot(projection="3d", computed_zorder=False)  # creates 3D plotting space so i can draw 3D graphs

for _ in range(300):
    x_derivative, y_derivative = calculate_gradient(curr_pos[0], curr_pos[1])
    x_new = curr_pos[0] - (learning_rate * x_derivative)
    y_new = curr_pos[1] - (learning_rate * y_derivative)

    curr_pos = (x_new, y_new, z_function(x_new, y_new))

    ax.plot_surface(X, Y, Z, cmap="viridis", zorder=0)  # prepares the drawing
    ax.scatter(curr_pos[0], curr_pos[1], curr_pos[2], color="red", zorder=1)

    plt.pause(0.001)
    ax.clear()