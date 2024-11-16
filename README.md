# Report on a Truly Autonomous Vehicle Solution

## WRO Season 2024 Future Engineers - Self-Driving Cars

Our team, **Driver US**, composed of passionate high school students from California, undertook the challenge of developing and creating an unique, innovative autonomous vehicle solution for the 2024 World Robot Olympiad (WRO) Future Engineers competition. This prestigious global competition tasked participants with designing, building, and programming a fully autonomous vehicle capable of navigating various obstacles, completing precision parking tasks, and dynamically adjusting to complex and ever-changing environments—all without any human intervention.

## Team Members and Roles

#### William Wu
A 10th-grade student passionate about coding from Rancho Cucamonga High School, [William](mailto:william1324230@gmail.com) oversaw the development and integration of AI algorithms. He ensured the AI system adapted to different track conditions and optimized the vehicle's performance in real time. His expertise in machine learning was instrumental in debugging and troubleshooting technical issues. By applying complex AI models, William played a crucial role in uniting the team and ensuring cohesive and efficient work throughout the project.

#### Yangxuezhe (Harry) Sun
A 11th-grade student with experience in programming and structural design from Rancho Cucamonga High School, [Yangxuezhe](mailto:sunyangxuezhe@gmail.com) assembled the physical vehicle and coded the algorithms enabling autonomous operation. His work focused on precise implementation of Pulse Width Modulation (PWM) for motor control, ensuring fine adjustments to the vehicle’s steering and speed. His work on the hardware part of the solution greatly helped put the project in motion and marked the start of the development of AI models.

#### Jiarui (Jerry) Hu
A 12th-grade student from Western Christian High School with extensive knowledge of artificial intelligence and 3D modeling, [Jiarui](mailto:epicericclass@gmail.com) was responsible for optimizing the AI system for real-time decision-making processes and editing videos for the team. He also helped organize the GitHub while maintaining a crucial role in supporting the team and making sure everythign was functioning. 

#### Coach Fei Guo
As a seasoned mentor with a background in autonomous systems, Coach Fei Guo provided invaluable guidance. He helped refine AI models and hardware integration while fostering critical and creative problem-solving skills within the team.
____________________________________________________________________________________________________________________________________
Together our synergy allowed us to work as a cohesive unit, overcoming obstacles and achieving milestones efficiently. By leveraging our combined expertise and supporting one another, we created a fully autonomous vehicle that not only met the competition’s rigorous requirements but also demonstrated the power of teamwork in advancing technological innovation.

## Technical Solution Design

Our vehicle’s design represents a careful combination of mechanical engineering, AI development, and control system integration, with a strong emphasis on robust, modular, and _Self-Designed_ hardware. The platform for the vehicle is an RC car ([Bezgar Remote Control Car](https://bezgar.com/products/hp161s-brushless-rc-monster-truck?srsltid=AfmBOooFGoxjODbHSdft2b3kG1eCqt0nHd6ybDr41GkETmGHhnId5QGx8ZQ)), chosen for its durability, speed, and reliability in high-performance environments. This base provided a sturdy foundation for handling the demanding tasks of the WRO competition.

We designed a modular [LEGO](https://simple.wikipedia.org/wiki/Lego#:~:text=LEGO%20bricks%20are%20colorful%20plastic,building%20toy%20in%20the%20world.) structure mounted atop the RC car to securely house the essential hardware components. The LEGO construction was chosen for its adaptability and standardization of parts, allowing us to make iterative adjustments during testing phases. This modularity proved critical when fine-tuning the positioning of the camera, gyroscope, and Raspberry Pi, ensuring optimal performance across varied track conditions and lighting environments.

At the heart of the vehicle lies the [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/), which served as the central processing unit (CPU). It processes data from the camera and gyroscope in real time, running AI models to make instantaneous decisions. The Raspberry Pi was selected for its computational power, compact size, and support for advanced machine learning frameworks such as TensorFlow. Most of the code is located on the raspberry pi inside a hard drive (SD card) and will be able to

The vehicle is equipped with a [Raspberry Pi Camera Module v2](https://www.raspberrypi.com/documentation/accessories/camera.html), which provides a live video feed of the track. This feed is critical for the AI system to recognize track boundaries, detect obstacles, and make informed navigational decisions. The camera was mounted on an adjustable LEGO arm, enabling precise positioning.

The [WT901 gyroscope](https://witmotion-sensor.com/products/9-axis-accelerometer-tilt-sensor-wt901-high-accuracy-acceleration-gyroscope-angle-magnetometer-with-kalman-filtering-triaxial-mpu9250-ahrs-imu-iic-ttl-200hz-for-pc-android-arduino?srsltid=AfmBOoqfCXdqwgJ5OLrF-OszHW7Pc291yX24ZmS6GENK0HButTmnNTTE) was integrated into the system to monitor the vehicle’s orientation and angular velocity. This sensor played a key role in determining when to stop the vehicle after 3 laps and monitored orientation data throughout the run. 

To achieve precise control over the vehicle’s movements, we implemented Pulse Width Modulation ([PWM with ic2 interface](https://www.adafruit.com/product/815)) for motor management. PWM allowed fine-tuned adjustments to the vehicle's speed and steering. This control system was essential for the raspberry pi to assimilate with the RC car and control it. Additionally, PWM optimized power consumption, ensuring reliable performance throughout extended competition runs.

To improve performance, the stock RC car tires were replaced with high-traction, off-road tires. These upgraded tires provided enhanced stability and grip on track surface and allowed it to make sharp turns without accidentally drifting off-course. 

By integrating these carefully selected hardware components into a cohesive design, our vehicle was able to handle the rigorous challenges of the WRO competition, demonstrating exceptional adaptability and performance in real-world scenarios.

## Software and Functionality of Codes

The software system for our autonomous vehicle is stored on an SD card within the Raspberry Pi. It consists of multiple Python scripts, each designed to handle specific tasks in the development, testing, and execution of the AI models. Below is a detailed breakdown of these code files:
* [manage.py](src/codes/Manage.py) is the main code that collects training data for the AI model
* [config.py](src/codes/config.py) defines the default Pulse Width Modulation (PWM) values, which are critical for controlling the vehicle's motors and steering. These parameters ensure consistent and precise vehicle movement.
* [calibrate.py](src/codes/Calibrate.py) is used to synchronize the AI model with the vehicle’s hardware, this script ensures that sensor data and system responses are accurately aligned during operation.
* [airc_drive10.py](src/codes/airc_drive10.py) serves as a testing tool for the AI model. It allows us to evaluate and debug the vehicle's performance in a controlled environment before deploying it in competition.
* [myconfig.py](src/codes/myconfig.py) provides the foundational framework upon which we built our customized AI solutions which is imported form the donkey car forums.
* [main_freerun.py](src/codes/main_freerun.py) is the final AI program for the freerun segment of the competition. This script enables the vehicle to autonomously complete three laps around the track and stop precisely based on gyroscope readings.
* [main_obstacle.py](src/codes/main_obstacle.py) is the final AI program for the obstacle run segment of the competition. It drives the car through two laps while dynamically avoiding obstacles according to the competition rules. The program then performs an additional lap (clockwise or counterclockwise as specified by the rules) and concludes with a final lap, parking the vehicle accurately in the designated slot.

These scripts seamlessly integrate with the electromechanical systems, including the Raspberry Pi, gyroscope, camera, and motors. Together, the software and hardware ensure a smooth and efficient training process, real-time decision-making, and flawless execution during competition. This harmonious interaction between software and hardware underscores the sophistication of our autonomous vehicle’s design.


## AI Training Process

The AI model for our autonomous vehicle was developed using real-world data collected during manual driving sessions on the competition track, facilitated by the script [manage.py](src/codes/Manage.py). These sessions enabled us to capture critical data, including camera images and vehicle control inputs, which served as the foundation for training the model.

To process this data, we used [FileZilla](https://filezilla-project.org) to transfer the training datasets from the Raspberry Pi to our development computers. Once the data was prepared, we leveraged [TensorFlow](https://www.tensorflow.org) within a [Miniconda3](https://docs.anaconda.com/miniconda/) command prompt environment to build and train a Convolutional Neural Network (CNN). The CNN was specifically designed to analyze visual inputs from the vehicle’s camera and map them to precise throttle and steering commands, enabling the AI to learn how to navigate the track effectively.

The training process was iterative, involving extensive testing and fine-tuning to optimize the model's accuracy and performance. After each iteration, we evaluated the AI's ability to handle various track scenarios, including straight paths, sharp turns, and obstacle navigation. With each improvement, the AI system became increasingly adept at interpreting visual inputs, making real-time decisions, and autonomously navigating the complex track conditions with precision.


## Power and Sense Management

Effective power management was essential to ensure reliable performance throughout the competition. To achieve this, Pulse Width Modulation (PWM) was employed to optimize the vehicle's power consumption, allowing us to extend battery life while maintaining consistent operation and precision control.

Our vehicle was powered by two sources:
* Li-Polymer Model 603048 (7.4V, 850mAh): This battery powered the RC car's motors, ensuring sufficient energy for movement and steering.
* HYD001 Portable Charger: This device powered the Raspberry Pi, which in turn supplied energy to the gyroscope and camera.

This power setup was carefully designed to ensure stability and reliability during operation. The modular structure allowed for efficient energy distribution across all components, providing sufficient power for extended competition runs and maintaining the system’s overall functionality.
____________________________________________________________________________________________________________________________________
















## Obstacle and Parking Management

The AI system was trained to recognize obstacles using visual data and to perform precise parking maneuvers. By analyzing the course layout and using control logic, the vehicle could navigate obstacles and park accurately within designated zones.

## Conclusion

Through this project, we developed a fully adaptive autonomous vehicle that meets the demands of the 2024 WRO Future Engineers competition. By integrating AI, machine learning, and engineering, we demonstrated the potential of autonomous systems in real-world applications. This experience has deepened our understanding of autonomous vehicle development and inspired us to further explore innovations in robotics and AI-driven technologies.
