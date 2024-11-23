'''
We used a python program called matplolib to create a better wiring diagram. To compile this you can download python on your computer and run it using VSC code. 
'''


import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow

# Function to draw wiring diagram
def draw_wiring_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')  # Hide axes

    # Add Raspberry Pi
    ax.text(6, 6.5, 'Raspberry Pi 4B', fontsize=12, ha='center')
    ax.add_patch(plt.Rectangle((5, 6), 2, 1, fill=False, edgecolor='black'))

    # Add Components
    components = {
        "160° FOV Camera": (3, 6),
        "WT901 Gyro Sensor": (9, 6),
        "Servo Motor": (3, 4),
        "DC Motor": (9, 4),
        "Electronic Speed Controller (ESC)": (6, 3),
        "Power Bank": (6, 7.5),
    }

    # Add rectangles and labels for components
    for label, (x, y) in components.items():
        ax.text(x, y + 0.4, label, fontsize=10, ha='center')
        ax.add_patch(plt.Rectangle((x - 0.5, y - 0.2), 1, 0.4, fill=False, edgecolor='blue'))

    # Draw Wires
    connections = [
        ((6, 6), (3, 6)),  # Pi to Camera
        ((6, 6), (9, 6)),  # Pi to Gyro
        ((6, 6), (3, 4)),  # Pi to Servo
        ((6, 6), (9, 4)),  # Pi to DC Motor
        ((6, 3), (9, 4)),  # ESC to DC Motor
        ((6, 7.5), (6, 6.5)),  # Power Bank to Pi
    ]

    for start, end in connections:
        ax.add_patch(FancyArrow(*start, *(end[0] - start[0], end[1] - start[1]),
                                width=0.01, length_includes_head=True, head_width=0.1, color='red'))

    plt.title("Reorganized Wiring Diagram", fontsize=14)
    plt.show()

# Call the function to draw the wiring diagram
draw_wiring_diagram()
