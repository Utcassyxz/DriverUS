# Report on a Truly Autonomous Vehicle Solution

## WRO Season 2024 Future Engineers - Self-Driving Cars

Our team, **Driver US**, composed of passionate high school students from California, undertook the challenge of developing and creating an unique, innovative autonomous vehicle solution for the 2024 World Robot Olympiad (WRO) Future Engineers competition. This prestigious global competition tasked participants with designing, building, and programming a fully autonomous vehicle capable of navigating various obstacles, completing precision parking tasks, and dynamically adjusting to complex and ever-changing environments—all without any human intervention.

## Team Members and Roles

#### William Wu
A 10th-grade student passionate about coding from Rancho Cucamonga High School, [William](mailto:william1324230@gmail.com) oversaw the development and integration of AI algorithms. He ensured the AI system adapted to different track conditions and optimized the vehicle's performance in real time. His expertise in machine learning was instrumental in debugging and troubleshooting technical issues. By applying complex AI models, William played a crucial role in uniting the team and ensuring cohesive and efficient work throughout the project.

#### Yangxuezhe (Harry) Sun
A 11th-grade student with experience in programming and structural design from Rancho Cucamonga High School, [Yangxuezhe](mailto:sunyangxuezhe@gmail.com) assembled the physical vehicle and coded the algorithms enabling autonomous operation. His work focused on precise implementation of Pulse Width Modulation (PWM) for motor control, ensuring fine adjustments to the vehicle’s steering and speed. His work on the hardware part of the solution greatly helped put the project in motion and marked the start of the development of AI models.

#### Jiarui (Jerry) Hu
A 12th-grade student from West Christian High School with extensive knowledge of artificial intelligence and 3D modeling, [Jiarui](mailto:epicericclass@gmail.com) was responsible for optimizing the AI system for real-time decision-making processes and editing videos for the team. He also helped organize the GitHub while maintaining a crucial role in supporting the team and making sure everythign was functioning. 

#### Coach Fei Guo
As a seasoned mentor with a background in autonomous systems, Coach Fei Guo provided invaluable guidance. He helped refine AI models and hardware integration while fostering critical and creative problem-solving skills within the team.
____________________________________________________________________________________________________________________________________
Together our synergy allowed us to work as a cohesive unit, overcoming obstacles and achieving milestones efficiently. By leveraging our combined expertise and supporting one another, we created a fully autonomous vehicle that not only met the competition’s rigorous requirements but also demonstrated the power of teamwork in advancing technological innovation.

## Technical Solution Design

Our vehicle’s design represents a careful combination of mechanical engineering, AI development, and control system integration, with a strong emphasis on robust, modular, and _Self-Designed_ hardware. The platform for the vehicle is an RC car ([Bezgar Remote Control Car](https://bezgar.com/products/hp161s-brushless-rc-monster-truck?srsltid=AfmBOooFGoxjODbHSdft2b3kG1eCqt0nHd6ybDr41GkETmGHhnId5QGx8ZQ)), chosen for its durability, speed, and reliability in high-performance environments. This base provided a sturdy foundation for handling the demanding tasks of the WRO competition.

We designed a modular [LEGO](https://simple.wikipedia.org/wiki/Lego#:~:text=LEGO%20bricks%20are%20colorful%20plastic,building%20toy%20in%20the%20world.) structure mounted atop the RC car to securely house the essential hardware components. The LEGO construction was chosen for its adaptability and standardization of parts, allowing us to make iterative adjustments during testing phases. This modularity proved critical when fine-tuning the positioning of the camera, gyroscope, and Raspberry Pi, ensuring optimal performance across varied track conditions and lighting environments.

At the heart of the vehicle lies the [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/), which served as the central processing unit (CPU). It processes data from the camera and gyroscope in real time, running AI models to make instantaneous decisions. The Raspberry Pi was selected for its computational power, compact size, and support for advanced machine learning frameworks such as TensorFlow.

The vehicle is equipped with a [Raspberry Pi Camera Module v2](https://www.raspberrypi.com/documentation/accessories/camera.html), which provides a live video feed of the track. This feed is critical for the AI system to recognize track boundaries, detect obstacles, and make informed navigational decisions. The camera was mounted on an adjustable LEGO arm, enabling precise positioning.

The [WT901 gyroscope](https://witmotion-sensor.com/products/9-axis-accelerometer-tilt-sensor-wt901-high-accuracy-acceleration-gyroscope-angle-magnetometer-with-kalman-filtering-triaxial-mpu9250-ahrs-imu-iic-ttl-200hz-for-pc-android-arduino?srsltid=AfmBOoqfCXdqwgJ5OLrF-OszHW7Pc291yX24ZmS6GENK0HButTmnNTTE) was integrated into the system to monitor the vehicle’s orientation and angular velocity. This sensor played a key role in determining when to stop the vehicle after 3 laps and monitored orientation data throughout the run. 

To achieve precise control over the vehicle’s movements, we implemented Pulse Width Modulation ([PWM with ic2 interface](https://www.adafruit.com/product/815)) for motor management. PWM allowed fine-tuned adjustments to the vehicle's speed and steering. This control system was essential for the raspberry pi to assimilate with the RC car and control it. Additionally, PWM optimized power consumption, ensuring reliable performance throughout extended competition runs.

To improve performance, the stock RC car tires were replaced with high-traction, off-road tires. These upgraded tires provided enhanced stability and grip on track surface and allowed it to make sharp turns without accidentally drifting off-course. 

By integrating these carefully selected hardware components into a cohesive design, our vehicle was able to handle the rigorous challenges of the WRO competition, demonstrating exceptional adaptability and performance in real-world scenarios.

## Software and Functionality of Codes

The software portion consists of code located on the raspberry pi in a SD card. Here is a breakdown for the different code files:
* Manage.py is the main code that allows for data training
* Config.py sets the the default PWM values which controls the car
* Calibrate.py allows for the synchronized processing of the AI model
* Airc_drive10.py is a testing software for the AI model
* Main_freerun.py is the final AI model program for our freerun part of the competition. The program drives the car 3 times around the track and stops based off gyro readings
* Main_obstacle.py is the final AI model program for our obstacle run part of the competition. The program drives the car 2 times around the track while dodging obstacels according the rules, completes another lap cw or ccw based off the rules, and compeltes a final lap that parks the car into the parking slot.

Overall the codes intertwine with the electromechanical designs to ensure a smooth functioning training process and model integration. 












_____________________________________________________________________________________________________________________________________













## AI Training Process

The AI model was trained using real-world data captured during manual driving sessions on a custom-built track. Using Google TensorFlow, we developed a Convolutional Neural Network (CNN) to interpret visual inputs from the camera and associate them with appropriate throttle and steering commands. After iterative testing and fine-tuning, the AI system became adept at navigating complex track conditions autonomously.

## Real-Time Decision Making

The AI system processed data from the camera and gyroscope in real time, enabling the vehicle to adjust its throttle, steering, and speed dynamically. This adaptability ensured smooth navigation of obstacles, sharp turns, and varying track conditions without human intervention.

## Power and Sensor Management

Effective power management was crucial for reliable performance. PWM was utilized to optimize power usage, extending battery life while maintaining consistent performance. The gyroscope and camera worked in tandem to provide real-time data for balance, orientation, and environmental awareness.

## Obstacle and Parking Management

The AI system was trained to recognize obstacles using visual data and to perform precise parking maneuvers. By analyzing the course layout and using control logic, the vehicle could navigate obstacles and park accurately within designated zones.

## Conclusion

Through this project, we developed a fully adaptive autonomous vehicle that meets the demands of the 2024 WRO Future Engineers competition. By integrating AI, machine learning, and engineering, we demonstrated the potential of autonomous systems in real-world applications. This experience has deepened our understanding of autonomous vehicle development and inspired us to further explore innovations in robotics and AI-driven technologies.
