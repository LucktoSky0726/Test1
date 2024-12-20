import matplotlib.pyplot as plt
import numpy as np

def plot_robot_direction(ax, x, directions):
    if not directions:
        return ax

    # Plot the starting point
    ax.plot(x, 0, 'o', color='red', markersize=3)

    current_x = x
    current_y = 0

    for dest_y, angle, line_style in directions:
        # Plot the main path
        ax.plot([current_x, current_x], [current_y, dest_y], color='blue', linewidth=8)

        # Plot the connecting path segments
        ax.plot([current_x, current_x], [current_y, dest_y], color='black', linewidth=1, linestyle=line_style)

        # Annotate the angle
        ax.text(current_x, current_y, f'{angle} degrees', fontsize=9, verticalalignment='bottom')

        # Update the current position
        current_y = dest_y

    return ax

# Example usage
fig, ax = plt.subplots()
directions = [(5, 45, '-'), (10, 90, '--'), (15, 135, '-.'), (20, 180, ':')]
plot_robot_direction(ax, 0, directions)
plt.xlim(-1, 1)
plt.ylim(-1, 21)
plt.show()