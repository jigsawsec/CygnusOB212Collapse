# Simulate the collapse process with rotation
collapse_steps = 10  # Number of steps in the collapse
collapse_factor = 0.1  # Factor by which the radius decreases in each step
rotation_angles = np.linspace(0, 2 * np.pi, collapse_steps)  # Rotation angles for each step

# Create a 3D plot for the collapse process
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

for step in range(collapse_steps):
    # Calculate the new radius
    radius = initial_radius * (1 - step * collapse_factor)
    
    # Generate new points on the surface of the collapsing sphere
    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(theta)
    
    # Apply rotation
    angle = rotation_angles[step]
    x_rot = x * np.cos(angle) - y * np.sin(angle)
    y_rot = x * np.sin(angle) + y * np.cos(angle)
    
    # Plot the collapsing and rotating star
    ax.scatter(x_rot, y_rot, z, alpha=0.6, label=f'Step {step + 1}')

# Plot the singularity (black hole)
ax.scatter(0, 0, 0, color='k', s=100, label='Singularity (Black Hole)')

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Formation of Black Hole from Cygnus OB2#12 Collapse')
ax.legend()

plt.show()
