'''
This program reads Z-axis angular velocity data from a WT901 gyroscope via I2C communication and calculates the yaw angle by 
integrating the gyroscope data over time (calculus concept). It includes:

Initialization: I2C communication setup, sensor address, and registers are defined.

Gyroscope Reading Function: Captures raw gyroscope data, processes it into degrees per second (dps), and handles the scaling.

Main Loop:
Reads gyro data.
Computes time differences between readings.
Updates yaw angle based on angular velocity and time elapsed.
Outputs the yaw angle in real-time.

Graceful Exit: Safely terminates on user interruption (e.g., pressing Ctrl+C)
'''

import smbus2
import time

# Import necessary modules:
# - smbus2: For I2C communication.
# - time: For tracking elapsed time in the program.

# I2C address of the WT901 sensor (default is 0x50)
DEVICE_ADDRESS = 0x50

# Register address for the Z-axis gyroscope data.
GYRO_Z_REGISTER = 0x39  # Example register for Z-axis gyroscope readings.

# Initialize the I2C bus for communication with the sensor.
bus = smbus2.SMBus(1)  # '1' refers to the I2C bus on the Raspberry Pi.

# Variable to store the calculated yaw angle based on gyroscope data.
yaw_angle = 0

# Initialize a time variable to track the previous reading's timestamp.
previous_time = time.time()

def read_gyro_z():
    """
    Reads the Z-axis angular velocity from the gyroscope via I2C.
    Returns the angular velocity in degrees per second.

    Steps:
    1. Read 2 bytes of data from the gyroscope Z-axis register.
    2. Combine the bytes into a signed 16-bit integer for raw gyro data.
    3. Convert raw data to angular velocity (dps) based on sensor scaling.
    """
    # Read two bytes from the gyro Z register
    data = bus.read_i2c_block_data(DEVICE_ADDRESS, GYRO_Z_REGISTER, 2)
    
    # Combine the two bytes into a 16-bit signed value.
    gyro_z_raw = data[1] << 8 | data[0]
    
    # Handle signed 16-bit values (convert to negative if needed).
    if gyro_z_raw > 32767:
        gyro_z_raw -= 65536
    
    # Scale the raw gyroscope value to degrees per second.
    # Assuming the sensor has a ±2000 degrees per second range.
    gyro_z = gyro_z_raw / 32768.0 * 2000  # Adjust scaling if needed for your sensor.
    return gyro_z

try:
    while True:
        """
        Main loop for reading gyroscope data and updating the yaw angle.
        
        Steps:
        1. Read the angular velocity (Z-axis) from the gyroscope.
        2. Apply a scaling correction if needed (for gyro drift or sensitivity adjustment).
        3. Calculate the elapsed time since the last reading.
        4. Update the yaw angle using the formula: angle += angular velocity * time.
        5. Print the current yaw angle to the console.
        6. Pause for a short interval (0.1 seconds) to avoid excessive readings.
        """
        # Read the current gyroscope value (Z-axis).
        gyro_z = read_gyro_z()
        
        # Apply a correction factor for improved accuracy (optional).
        if gyro_z > 0:
            gyro_z = gyro_z * 1.008

        # Get the current time.
        current_time = time.time()

        # Calculate time difference (delta t) since the last reading.
        delta_t = current_time - previous_time

        # Update the yaw angle by integrating angular velocity over time.
        yaw_angle += gyro_z * delta_t

        # Update the timestamp for the next calculation.
        previous_time = current_time

        # Print the current yaw angle to the console.
        print("Yaw Angle: {:.2f} degrees".format(yaw_angle))

        # Pause briefly before the next reading (reduce processing load).
        time.sleep(0.1)

except KeyboardInterrupt:
    """
    Handle program interruption (e.g., Ctrl+C).
    Safely exit the program and notify the user.
    """
    print("Program interrupted")
