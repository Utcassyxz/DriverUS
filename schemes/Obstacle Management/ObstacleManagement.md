# Obstacle Management

## Freerun 
In the freerun segment of the competition, our vehicle’s obstacle management system was designed to navigate three laps around the track while maintaining consistent speed and steering precision. Although the freerun course did not include obstacles, the challenge lay in the vehicle's ability to interpret track boundaries, adapt to varying lighting conditions, and ensure precise control over its trajectory. The Raspberry Pi Camera Module v2 played a pivotal role by capturing real-time video feed of the track, which was processed by the AI model trained on convolutional neural networks (CNN). This model enabled the vehicle to distinguish track edges and remain within the defined path throughout the course.

The gyroscope was equally critical, ensuring the vehicle maintained stability and proper orientation during sharp turns and straight paths. By leveraging angular velocity data, the vehicle dynamically adjusted its steering to achieve optimal turning radii without losing traction or control. Additionally, the gyroscope allowed the vehicle to monitor its progress and execute a precise stop after completing three laps, fulfilling the freerun requirements with accuracy. Our software system, driven by scripts such as main_freerun.py, ensured seamless integration between hardware and AI, allowing for flawless performance during this segment of the competition.

## Obstacle Run and Parking
The obstacle run and parking segment of the competition posed a far greater challenge, requiring the vehicle to autonomously navigate a track populated with stationary obstacles, perform specific maneuvers, and accurately park in the designated slot. For this segment, we relied heavily on a combination of sensory input, advanced AI algorithms, and pre-defined logic to meet the rules and constraints of the competition. The Raspberry Pi Camera Module v2 provided continuous visual feedback, enabling the AI model to detect and classify obstacles on the track. The AI system dynamically adjusted the vehicle’s speed and steering to avoid collisions, carefully recalibrating its trajectory to maneuver around obstacles with precision.

The gyroscope was instrumental in maintaining the vehicle's orientation during complex maneuvers, particularly when avoiding tightly placed obstacles. By monitoring angular velocity and tilt, the gyroscope ensured the vehicle stayed balanced and correctly oriented, even during abrupt directional changes. Our software, main_obstacle.py, executed a sophisticated set of commands, enabling the vehicle to complete two laps of obstacle avoidance with flawless accuracy.

Upon completing the two initial laps, the vehicle was programmed to perform an additional lap, either clockwise or counterclockwise as specified by competition rules. This segment demonstrated the system's adaptability, as it required the AI to dynamically shift its logic to handle varying directions and obstacles on the fly. Following the final lap, the vehicle entered the designated parking zone. The gyroscope data, combined with pre-calibrated AI parameters, allowed the vehicle to execute a precise stop within the parking area, adhering to competition guidelines.

By integrating high-performance hardware, robust AI algorithms, and a meticulous calibration process, our vehicle’s obstacle management system excelled in both freerun and obstacle segments. It demonstrated an ability to handle complex track scenarios while adhering to the stringent rules of the WRO competition, showcasing the sophistication and reliability of our design.




