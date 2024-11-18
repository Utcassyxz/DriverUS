# Electromechanical Diagrams and Component Descriptions

## **Electromechanical Diagrams**

Electromechanical diagrams for an AI RC Car incorporate a Raspberry Pi, PWM signals, and TensorFlow, illustrating connections and interactions between electrical and mechanical components. These diagrams are essential for designing, building, troubleshooting, and maintaining the car. Below is an overview of the key diagram types and their roles.

### **Types of Diagrams**

1. **Schematic Diagrams**  
   - Illustrate logical flow and connections of electrical components.  
   - Show how the Raspberry Pi connects to sensors, motor drivers, and the power supply, including PWM signal control for motors.

2. **Wiring Diagrams**  
   - Detail the physical connections and layout of wires and components.  
   - Highlight connections between sensors and Raspberry Pi GPIO pins, motor drivers to motors, and power supply distribution.

3. **Pictorial Diagrams**  
   - Use images or drawings to depict the physical appearance and arrangement of components.  
   - Include the placement of the Raspberry Pi, sensors, motor drivers, and the power supply in the RC car.

4. **Block Diagrams (Flowcharts)**  
   - Simplify the system into blocks representing functional sections, such as AI processing, sensor array, motor control, and power management.  
   - Provide a high-level overview of system operations without detailing wiring specifics.

---

## **Components in AI RC Car Diagrams**

### **Raspberry Pi**
- **Description**: A small, versatile computer ideal for electronics and robotics projects. 
- **Role**: Runs TensorFlow models, processes camera feeds, and controls the car’s motors and sensors. Serves as the main computing power in our vehicle and is essential for our project.

### **Pi Camera**
- **Description**: A high-definition camera module connected via the Raspberry Pi's CSI port.  
- **Role**: Serves as the car’s "eyes," capturing images for AI training and real-time navigation.

### **PWM (Pulse Width Modulation)**
- **Description**: Controls power delivery by varying the duty cycle of on/off signals.  
- **Role**: Regulates motor speed (throttle) and steering angle based on AI predictions. Allows for the Raspberry Pi to connect to the RC car for motor control without the need for an off-the-shelf car + computer system. 

### **GPIO (General Purpose Input/Output)**
- **Description**: Programmable pins on the Raspberry Pi are used to control and communicate with other components.  
- **Role**: Enables interaction with motors, sensors, and displays. Allows for the connection from the Raspberry Pi to the to the PWM system and the ability to have an on/off switch.

### **On/Off Switch**
- **Description**: Switch wired to the Raspberry Pi that sends data based on whether it's turned on or off.  
- **Role**: Key component in our vehicle where we programmed the Raspberry Pi to automatically run the AI model when the switch is turned on. This helps our vehicle satisfy the one-switch rule designated by WRO. The switch is connected to the ground and GPIO 25 on the GPIO pins on the Raspberry Pi. 

### **Gyroscope**
- **Description**: Sensor that measures orientation and rotation.  
- **Role**: Tracks the car’s position and movement, assisting in model switching and adaptive driving behavior. Is used in our code to determine how many laps that vehicle has committed and sets a stop condition for the robot. 

### **LCD 1602**
- **Description**: A small screen displaying up to two lines of 16 characters each.  
- **Role**: Shows AI model status, gyroscope data, and system updates. Is used to initially run the robot program when the Raspberry Pi is turned on and allows us to see a small portion of the Raspberry Pi screen without us connecting to it directly. 

### **RC Car**
- **Description**: A remote-controlled car platform.  
- **Role**: Provides the physical base for testing AI models and sensors.

### **Lego Pieces**
- **Description**: Modular building components from the LEGO EV3 set.  
- **Role**: Create a lightweight, adjustable structure for securely holding the Raspberry Pi, camera, and sensors. Provides great adaptability in the early design stages of the project and offers a centralized structure that can be altered at any time. 

---

## **Applications of Electromechanical Diagrams**

Electromechanical diagrams are essential for:  
- **Designing**: Planning layouts and connections.  
- **Assembling**: Guiding physical construction and wiring.  
- **Troubleshooting**: Identifying and resolving system issues.  
- **Maintaining**: Ensuring consistent functionality through regular checks and updates.

---

This document highlights the importance of diagrams and components in creating a robust AI RC Car system, ensuring a clear understanding and seamless collaboration across design, assembly, and operational phases.
