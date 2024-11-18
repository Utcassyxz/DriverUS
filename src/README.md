# Control Software and Obstacle Management

## Core Technologies

### **Python**
Python serves as the backbone of the control software, renowned for its simplicity and versatility. It powers hardware interfacing, real-time data processing, and advanced machine learning integration, enabling a robust and efficient system for the AI RC Car.

### **TensorFlow**
As a cutting-edge open-source machine learning framework, TensorFlow enables the design and training of sophisticated AI models. It equips the AI RC Car with neural networks for object recognition, decision-making, and autonomous navigation, ensuring adaptability in dynamic and challenging environments.

### **FileZilla**
A powerful file transfer application that streamlines communication between the Raspberry Pi and other devices. FileZilla ensures secure and efficient file transfer, supporting seamless development and remote management of the RC Car.

### **realVNC**
RealVNC provides a wireless interface for accessing and controlling the Raspberry Pi from a computer. This tool enhances flexibility and development efficiency by allowing users to monitor and adjust the car's operations remotely, enabling real-time problem-solving and fine-tuning.


## Key Components

### **Calibrate**
The calibration process is crucial for aligning sensors and motors, ensuring accurate data collection and precise movement. This step optimizes the car's performance across various conditions, laying the groundwork for smooth and reliable operation.

### **Config**
The central configuration hub contains critical parameters like sensor thresholds, motor speed limits, and AI model hyperparameters. This module enables quick and effective adjustments to tailor the system for specific tasks or environments. Our RC car base model is set able to run at up to 40 mph (according to the supplier) but for the sake of our competition we limited it to a maximum of 3 mph. 

### **Manage**
A robust management framework that oversees the AI RC Car's entire operation. It monitors system health, ensures efficient communication between components, and coordinates all functionalities for seamless autonomous performance. Our Manage.py model was built off of the donkey car base code from the forums and is one of the more simple programs that we have. 

### **myconfig**
A customizable configuration file that stores user-defined preferences and specific environment settings. This personalization layer adapts the car’s behavior to unique challenges, enhancing flexibility and performance.

### **Train**
This module leverages TensorFlow to iteratively train AI models, optimizing neural networks using extensive datasets. It focuses on refining decision-making algorithms, enhancing the car’s autonomous capabilities through continuous improvement.

---

## Enhanced Workflow Process

### **1. Workflow Configuration**
The initial setup leverages the `config` and `myconfig` modules to tailor the car's system parameters and settings to the target environment, ensuring optimal readiness.

### **2. Calibration**
Sensor and motor calibration fine-tunes the hardware for precision and responsiveness. Accurate calibration is critical to achieving dependable performance and adapting to variable conditions.

### **3. Training**
Using TensorFlow, the AI models are trained through data-driven optimization. This iterative process refines neural network parameters to improve decision-making, navigation, and obstacle management.

### **4. Deployment**
With the help of FileZilla, the trained AI models and updated software are deployed to the Raspberry Pi. This process allows for real-time software updates and remote management.

### **5. Operation**
The `Manage` module seamlessly integrates the AI models, sensors, and motors, coordinating their actions to achieve precision in autonomous navigation and environmental interaction.

---

This streamlined and powerful system ensures that the AI RC Car achieves peak performance, embodying innovation and precision in the WRO Future Engineers competition. Our part sourcing is also listed below:

**Parts**

* [Bezgar Remote Control Car](https://bezgar.com/products/hp161s-brushless-rc-monster-truck?srsltid=AfmBOooFGoxjODbHSdft2b3kG1eCqt0nHd6ybDr41GkETmGHhnId5QGx8ZQ) - RC car model 🚗
* [LEGO](https://simple.wikipedia.org/wiki/Lego#:~:text=LEGO%20bricks%20are%20colorful%20plastic,building%20toy%20in%20the%20world.) - Container for other parts on top of RC car 📦
* [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/) - Brain of the vehicle 🧠
* [Raspberry Pi Camera Module v2](https://www.raspberrypi.com/documentation/accessories/camera.html) - Eyes of the vehicle 👀
* [WT901 gyroscope](https://witmotion-sensor.com/products/9-axis-accelerometer-tilt-sensor-wt901-high-accuracy-acceleration-gyroscope-angle-magnetometer-with-kalman-filtering-triaxial-mpu9250-ahrs-imu-iic-ttl-200hz-for-pc-android-arduino?srsltid=AfmBOoqfCXdqwgJ5OLrF-OszHW7Pc291yX24ZmS6GENK0HButTmnNTTE) - Sense of direction for the vehicle 🧭
* [16 channel 12-bit PWM Servo Driver I2C](https://www.adafruit.com/product/815) - Mechanical controller 🤖
* [Li-Polymer Model 603048 (7.4V, 850mAh)](https://usa.banggood.com/ZOP-Power-7_4V-850mAh-100C-2S-LiPo-Battery-XT30-Plug-for-RC-Drone-p-1978448.html?utm_source=googleshopping&utm_medium=cpc_organic&gmcCountry=US&utm_content=minha&utm_campaign=aceng-pmax-usg-pc&currency=USD&cur_warehouse=CN&createTmp=1) - Powers the RC car 🔋
* [HYD001 Portable Charger](https://manuals.plus/miady/miady-hyd001-power-bank-user-manual) - Powers the raspberry pi and rest of the sensors 🪫
* [Kcd1-11 Switch](https://www.finglai.com/products/switches/rocker-switches/KCD1-KCD5-13.5x9/KCD1-11-2P-UB.html) - On/off switch for the robot 😴
* [GPIO Wires](https://forums.raspberrypi.com/viewtopic.php?t=216304) - Connects PWM to RC car and and raspberry pi and the raspberry pi to the gyro 🔗
* [GPIO cables](https://www.raspberrypi.com/products/camera-cable/) - Connects the raspberry pi camera to the raspberry pi 🖇️






