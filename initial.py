import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the initial parameters for Cygnus OB2#12
initial_radius = 1  # Arbitrary units for visualization
num_particles = 1000  # Number of particles to represent the star

# Generate random points on the surface of a sphere to represent the star
theta = np.random.uniform(0, np.pi, num_particles)
phi = np.random.uniform(0, 2 * np.pi, num_particles)
x = initial_radius * np.sin(theta) * np.cos(phi)
y = initial_radius * np.sin(theta) * np.sin(phi)
z = initial_radius * np.cos(theta)

# Create a 3D plot for the initial state of the star
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, color='b', alpha=0.6, label='Cygnus OB2#12')

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Initial State of Cygnus OB2#12')
ax.legend()

plt.show()
