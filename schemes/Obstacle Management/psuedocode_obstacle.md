```
Initialize Pi Camera and load trained model
Start capturing frames continuously

While True:
    Capture a frame from the camera
    Process the frame using the TensorFlow model
    Monitor gyroscope to determine when 3 laps are reached

    If an obstacle is detected:
        Calculate the distance and direction to the obstacle
        Determine if the car should go left or right based on obstacle location
        Adjust steering and throttle to avoid the obstacle
    Else:
        Continue along the default path

    If gyro detects 2 laps and camera detects red:
        Turn around and run another obstacle lap.
        Initialize parking model:
            If the parking zone is detected:
                Slow down and align to park
                Stop when parked
    Else if gyro detects 2 laps and camera detects green:
        Continue to run the obstacle run for one lap
        Initialize parking model:
            If the parking zone is detected:
                Slow down and align to park
                Stop when parked
    
End
```
