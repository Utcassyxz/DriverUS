# Obstacle Management

## Freerun 
In the freerun segment of the competition, our vehicle’s obstacle management system was designed to navigate three laps around the track while maintaining consistent speed and steering precision. Although the freerun course did not include obstacles, the challenge lay in the vehicle's ability to interpret track boundaries, adapt to varying lighting conditions, and ensure precise control over its trajectory. The Raspberry Pi Camera Module v2 played a pivotal role by capturing real-time video feed of the track, which was processed by the AI model trained on convolutional neural networks (CNN). This model enabled the vehicle to distinguish track edges and remain within the defined path throughout the course.

The gyroscope was equally critical, ensuring the vehicle maintained stability and proper orientation during sharp turns and straight paths. By leveraging angular velocity data, the vehicle dynamically adjusted its steering to achieve optimal turning radii without losing traction or control. Additionally, the gyroscope allowed the vehicle to monitor its progress and execute a precise stop after completing three laps, fulfilling the freerun requirements with accuracy. Our software system, driven by scripts such as main_freerun.py, ensured seamless integration between hardware and AI, allowing for flawless performance during this segment of the competition.

## Obstacle Run and Parking





