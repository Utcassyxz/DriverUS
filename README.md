# Report on a Truly Autonomous Vehicle Solution

## WRO Season 2024 Future Engineers - Self-Driving Cars

Our team, **Driver US**, composed of passionate high school students from California, undertook the challenge of developing and creating an unique, innovative autonomous vehicle solution for the 2024 World Robot Olympiad (WRO) Future Engineers competition. This prestigious global competition tasked participants with designing, building, and programming a fully autonomous vehicle capable of navigating various obstacles, completing precision parking tasks, and dynamically adjusting to complex and ever-changing environments—all without any human intervention.

## Team Members and Roles

#### William Wu
A 10th-grade student passionate about coding from Rancho Cucamonga High School, William oversaw the development and integration of AI algorithms. He ensured the AI system adapted to different track conditions and optimized the vehicle's performance in real time. His expertise in machine learning was instrumental in debugging and troubleshooting technical issues. By applying complex AI models, William played a crucial role in uniting the team and ensuring cohesive and efficient work throughout the project.

#### Yangxuezhe (Harry) Sun
A 11th-grade student with experience in programming and structural design from Rancho Cucamonga High School, Yangxuezhe assembled the physical vehicle and coded the algorithms enabling autonomous operation. His work focused on precise implementation of Pulse Width Modulation (PWM) for motor control, ensuring fine adjustments to the vehicle’s steering and speed. His work on the hardware part of the solution greatly helped put the project in motion and marked the start of the development of AI models.

#### Jiarui (Jerry) Hu
A 12th-grade student from West Christian High School with extensive knowledge of artificial intelligence and 3D modeling, Jiarui was responsible for optimizing the AI system for real-time decision-making processes and editing videos for the team. He also helped organize the GitHub while maintaining a crucial role in supporting the team and making sure everythign was functioning. 

#### Coach Fei Guo
As a seasoned mentor with a background in autonomous systems, Coach Fei Guo provided invaluable guidance. He helped refine AI models and hardware integration while fostering critical and creative problem-solving skills within the team.
____________________________________________________________________________________________________________________________________
Together our synergy allowed us to work as a cohesive unit, overcoming obstacles and achieving milestones efficiently. By leveraging our combined expertise and supporting one another, we created a fully autonomous vehicle that not only met the competition’s rigorous requirements but also demonstrated the power of teamwork in advancing technological innovation.

## Technical Solution Design

Our vehicle’s design represents a careful combination of mechanical engineering, AI development, and control system integration, with a strong emphasis on robust, modular, and _Self-Designed_ hardware. The platform for the vehicle is an RC car ([Bezgar Remote Control Car](https://bezgar.com/products/hp161s-brushless-rc-monster-truck?srsltid=AfmBOooFGoxjODbHSdft2b3kG1eCqt0nHd6ybDr41GkETmGHhnId5QGx8ZQ)), chosen for its durability, speed, and reliability in high-performance environments. This base provided a sturdy foundation for handling the demanding tasks of the WRO competition.

We designed a modular LEGO structure mounted atop the RC car to securely house the essential hardware components. The LEGO construction was chosen for its adaptability and standardization of parts, allowing us to make iterative adjustments during testing phases. This modularity proved critical when fine-tuning the positioning of the camera, gyroscope, and Raspberry Pi, ensuring optimal performance across varied track conditions and lighting environments.

At the heart of the vehicle lies the Raspberry Pi 4 Model B, which served as the central processing unit (CPU). It processed data from the camera and gyroscope in real time, running AI models to make instantaneous decisions. The Raspberry Pi was selected for its computational power, compact size, and support for advanced machine learning frameworks such as TensorFlow.



_____________________________________________________________________________________________________________________________________









Our vehicle’s design combined mechanical engineering, AI development, and control system integration. Starting with an RC car platform, we replaced stock tires with robust ones to enhance stability and maneuverability on challenging tracks. We added a modular LEGO structure atop the RC car to house key components such as the Raspberry Pi, camera, and gyroscope.

The **Raspberry Pi** served as the central processing unit, integrating data from the camera and gyroscope in real time. This allowed the AI system to make decisions dynamically. **Pulse Width Modulation (PWM)** was employed for precise motor control, ensuring smooth navigation and optimized power consumption.

## Software and Functionality of Codes

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
