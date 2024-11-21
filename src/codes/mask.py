'''
This code captures and processes live video frames using a Raspberry Pi camera to detect the presence of red or green colors. 
Implemented in the obstacle run to mask out distractions and only see red/green colors
'''

# Initial imports
import cv2
import numpy as np
import time
from picamera2 import Picamera2
from libcamera import Transform

# Initialize PiCamera
config_dict = {"size": (160, 120), "format": "BGR888"}  # Camera resolution and format
transform = Transform(False, False)  # Define camera transformation (no flipping)
camera = Picamera2()  # Create a camera instance
config = camera.create_preview_configuration(config_dict, transform=transform)  # Configure the camera
camera.align_configuration(config)  # Align the configuration settings
camera.configure(config)  # Apply the configuration
camera.set_controls({"FrameDurationLimits": (100, 1000)})  # Set frame duration limits (slower frame rate)
camera.start()  # Start the camera

# Initialize frame and control variables
frame = None  # Variable to store the captured frame
on = True  # Control flag (currently unused)
image_d = 3  # Image dimension identifier (currently unused)

# Allow the camera to warm up
time.sleep(0.5)

# Define HSV color ranges for green and red
lower_green = np.array([36, 100, 100])  # Lower HSV bound for green
upper_green = np.array([86, 255, 255])  # Upper HSV bound for green
lower_red2 = np.array([165, 150, 100])  # Lower HSV bound for red
upper_red2 = np.array([179, 255, 255])  # Upper HSV bound for red

counter = 0  # Frame counter (currently unused)
start_time = time.time()  # Start time for frame rate calculation (currently unused)

# Continuously capture frames from the camera
while True:
    # Capture a frame as a NumPy array
    frame = camera.capture_array("main")
    
    # Convert the frame to BGR color space (required for OpenCV processing)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    image = frame
    
    # Convert the frame to HSV color space for color detection
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Create binary masks for green and red colors
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)  # Green mask
    mask_red = cv2.inRange(hsv_image, lower_red2, upper_red2)  # Red mask
    
    # Count the number of non-zero pixels in each mask
    red_count = cv2.countNonZero(mask_red)  # Count red pixels
    green_count = cv2.countNonZero(mask_green)  # Count green pixels
    
    # Detect the dominant color based on pixel counts
    if red_count > green_count and red_count > 100:  # Threshold to filter noise
        print("Red detected")
    elif green_count > red_count and green_count > 100:  # Threshold to filter noise
        print("Green detected")
    else:
        print("No red or green detected")  # No dominant color detected
    
    # Display the current frame (optional, useful for debugging)
    cv2.imshow("Frame", image)
    
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up resources
cv2.destroyAllWindows()  # Close all OpenCV windows
camera.close()  # Stop and release the camera
