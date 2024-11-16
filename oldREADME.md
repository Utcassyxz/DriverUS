Report on a Truely Autonomous Vehicle Solution:

WRO Season 2024 Future Engineers - Self-Driving Cars

Our team, Driver US, composed of passionate high school students from Rancho Cucamonga, California, undertook the challenge of developing an innovative autonomous vehicle solution for the 2024 World Robot Olympiad (WRO) Future Engineers competition. This prestigious global competition tasked participants with designing, building, and programming a fully autonomous vehicle capable of navigating various obstacles, completing precision parking tasks, and dynamically adjusting to complex and ever-changing environments—all without any human intervention.

The WRO Future Engineers competition provided us with a rare and exciting opportunity to apply theoretical knowledge to real-world problems, merging disciplines such as robotics, artificial intelligence (AI), machine learning, and engineering. This project allowed us to push the boundaries of innovation and to showcase how AI can be integrated into mechanical systems for the purpose of achieving autonomous control.

Our journey toward building this autonomous vehicle was not only a lesson in programming or hardware design but also a deep dive into the complexities of how AI and machine learning can be applied to improve decision-making processes in real time. Through this experience, we gained hands-on knowledge in hardware development, AI integration, and system design. More importantly, the project has allowed us to contribute, albeit in a small way, to the future of autonomous transportation systems and robotics, with potential applications far beyond the scope of this competition.

Team Members and Roles:

One of the key elements of our team’s success was the diversity of talents and skills brought by each member. Every individual contributed uniquely to the overall project, bringing together different perspectives, expertise, and problem-solving approaches to develop a cohesive and adaptive solution.

Yangxuezhe Sun: an 11th-grade student passionate about coding, took on the critical role of overseeing the development and integration of the AI algorithms. His leadership unite the team. In this domain, he ensured that the AI system adapted to different track conditions, which helped optimize the vehicle's performance in real time. His expertise in machine learning proved invaluable in debugging and troubleshooting the technical issues that arose during development. By applying complex AI models, Yangxuezhe played a crucial role in ensuring the team worked cohesively and efficiently throughout the project’s lifecycle.

Jiarui Hu: a 12th-grade student with extensive knowledge of artificial intelligence and 3D modeling, was responsible for optimizing the AI system for real-time decision-making processes. Jiarui fine-tuned the vehicle’s decision-making abilities based on camera inputs. In addition to his AI development role, Jiarui also used 3D modeling software to simulate the vehicle’s behavior before any real-world implementations. This critical step allowed the team to visualize how the AI and mechanical systems would interact before moving to physical testing.

William Wu: a 10th-grade student with experience in both programming and structural design, was responsible for assembling the physical vehicle and coding the algorithms that allowed the car to operate autonomously. His work focused on the precise implementation of Pulse Width Modulation (PWM), which controlled the motors, enabling fine adjustments to the vehicle’s steering and speed. William’s attention to detail in both coding and vehicle assembly ensured that the robot maintained structural integrity and consistent performance throughout the competition.

Coach Fei Guo: brought a wealth of experience in robotics and engineering to the project. As a seasoned mentor with a background in autonomous systems, Coach Guo helped the team refine AI models and hardware integration. His guidance fostered a creative and problem-solving mindset among the team members, encouraging them to think critically when tackling the challenges that arose during the project’s development.

Technical Solution Design:

Our vehicle’s design combined several complex fields: mechanical engineering, AI development, and control system integration. The process began with the selection of a base platform for the robot: an RC car, chosen for its durability and reliable performance in fast-paced environments. We replaced the stock tires with more robust ones to improve stability, grip, and maneuverability on the challenging competition tracks. These modifications enhanced the car’s traction and control, particularly when navigating tight turns, uneven surfaces, and steep gradients, which were common obstacles in the WRO competition.

In addition to upgrading the vehicle's wheels, we constructed a modular LEGO structure atop the RC car. This structure securely held critical components such as the Raspberry Pi, camera, and gyroscope. The modular design allowed us to make iterative adjustments during testing phases, especially to the adjustable camera mount. The camera’s positioning had to be fine-tuned based on specific lighting conditions and track layouts, and the modular setup made these adjustments seamless. By engineering a flexible hardware configuration, we significantly improved the vehicle's overall performance in each phase of the competition.

The Raspberry Pi served as the vehicle’s central processing unit (CPU), collecting and processing data from the camera and gyroscope in real time. The gyroscope provided the AI system with critical data on the car’s orientation and balance, while the camera captured live video feed essential for recognizing track boundaries, obstacles, and environmental features. The integration of these sensors with the AI system allowed the vehicle to make real-time decisions, navigate complex environments autonomously, and adjust its behavior based on changing conditions.

We employed Pulse Width Modulation (PWM) as the primary method of controlling the vehicle’s motors. PWM gave us precise control over the car’s throttle and steering, which was critical for making smooth adjustments to the vehicle’s speed and direction, particularly when navigating tight turns or avoiding obstacles. In addition to improving control, PWM also allowed us to optimize the vehicle’s power consumption, ensuring consistent performance and avoiding performance drops during longer competition runs.

AI Training Process:

Developing the AI model for autonomous driving was one of the most challenging yet rewarding aspects of our project. The AI’s ability to make real-time decisions was key to the vehicle’s performance, and this required extensive training using real-world data.

We began the AI training process by manually driving the car through a custom-built track that mimicked the conditions of the WRO competition. During these manual driving sessions, the camera mounted on the vehicle captured images of the track, while the Raspberry Pi recorded the car’s throttle, steering angle, and speed. This data formed the foundation of the AI’s training set.

After collecting a sufficient amount of training data, we used Google TensorFlow to build a Convolutional Neural Network (CNN). The CNN was trained to interpret visual patterns from the camera input and associate them with appropriate throttle and steering commands. In essence, the AI learned how to react to various track conditions—such as straight paths, sharp turns, and obstacle-laden sections—based on the data from these manual driving sessions.

The manual driving sessions allowed the camera to document the track in real-time, and the CNN processed these visual inputs to make decisions during autonomous driving. For instance, when the AI detected a sharp turn based on the image input, it would adjust the vehicle’s throttle and steering based on the behaviors learned during training. This process allowed the AI to autonomously navigate the track with increasing accuracy over time.

The training process involved multiple iterations of testing and fine-tuning. After each round of testing, we reviewed the vehicle’s performance and adjusted the AI model’s parameters to improve its decision-making accuracy. Over time, the AI system became more adept at processing visual input and making real-time decisions, which minimized the need for human intervention during competition runs.

Real-Time Decision Making:

A major strength of our project was the AI system’s ability to process data from the camera and gyroscope in real time and make decisions without human input. During each competition run, the camera continuously captured images of the track, which were then analyzed by the CNN to identify key features such as track boundaries, obstacles, and sharp turns. The AI system used this information to adjust the vehicle’s throttle, steering, and speed accordingly.

For example, if the AI detected an obstacle in its path, it would calculate the best course of action—whether to slow down, steer around the obstacle, or stop altogether to avoid a collision. Similarly, when the AI encountered a sharp turn, it could reduce the throttle and adjust the steering angle to ensure that the vehicle navigated the turn smoothly and without losing balance.

The ability of the AI to make these real-time decisions was critical to the vehicle’s overall performance, allowing it to respond dynamically to the environment. This adaptability ensured that the vehicle could handle unexpected situations, such as sudden obstacles or variations in track conditions, with minimal delays or errors.

Power and Sensor Management:

Power management was another crucial aspect of our vehicle’s design, as it directly impacted the vehicle’s reliability and performance during competition runs. The vehicle’s battery needed to supply power to both the motor and the Raspberry Pi, and careful power management was essential to prevent performance drops or battery depletion during longer runs.

By using Pulse Width Modulation (PWM), we optimized the vehicle’s power usage, ensuring that the motor consumed only the necessary amount of energy for each task. This approach allowed us to extend the vehicle’s battery life while maintaining consistent performance throughout the competition.

The vehicle’s sensors, particularly the gyroscope and camera, played a vital role in providing real-time data to the AI system. The gyroscope ensured that the car remained balanced during high-speed movements and tight turns, while the camera provided continuous visual feedback about the vehicle’s surroundings. These sensors worked together to give the AI the data it needed to make quick and informed decisions about the vehicle’s movements.

Obstacle and Parking Management:

Navigating obstacles and performing precise parking maneuvers were among the most difficult challenges presented by the WRO competition. To tackle these tasks, our AI system was trained to recognize obstacles using the visual data captured by the camera. Once an obstacle was detected, the AI analyzed the image and determined the best course of action, whether to slow down, steer away, or stop.

In addition to navigating obstacles, the vehicle also needed to perform precise parking maneuvers. The AI system used control logic to guide the car into designated parking zones by analyzing the course layout and adjusting the vehicle’s speed and direction accordingly. The use of PWM allowed for fine control over the vehicle’s speed, ensuring that the vehicle could park accurately within the required boundaries.

By training the AI system to handle both obstacle avoidance and precision parking, we ensured that the vehicle was capable of performing all tasks required for a successful competition run.

Conclusion:

Through this project, we developed a fully adaptive autonomous vehicle capable of navigating complex environments, avoiding obstacles, and performing precise maneuvers—all without human intervention. By leveraging AI, machine learning, and engineering, we successfully built a vehicle that not only met the demands of the 2024 WRO Future Engineers competition but also showcased the potential of autonomous systems in real-world applications.

The experience gained through this project has broadened our understanding of the challenges and opportunities in autonomous vehicle development, and we are excited to continue exploring this field. Whether through further refinement of our AI model or future innovations in robotics, we look forward to contributing to the exciting future of autonomous systems and AI-driven technologies.
