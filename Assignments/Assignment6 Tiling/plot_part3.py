import os
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

filename = 'costToGo.npy'
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
if os.path.exists(filename):
    Z = np.load(filename)
    pos = np.arange(-1.2, 0.5, 1.7/ 50.0)
    vel = np.arange(-0.07, 0.07, 0.14 / 50.0)
    X = np.zeros((50))
    Y = np.zeros((50))

    X, Y = np.meshgrid(pos, vel)
    
    ax.plot_wireframe(X, Y, Z)

    ax.set_xlabel('Position')
    ax.set_ylabel('Velocity')
    ax.set_zlabel('cost to go')
    plt.show()