# Control Software and Obstacle Management

## Core Technologies

### **Python**
The core programming language driving the control software, Python offers unparalleled simplicity and versatility. Its rich ecosystem of libraries is leveraged for hardware interfacing, real-time data processing, and the implementation of cutting-edge machine learning algorithms.

### **TensorFlow**
An advanced, open-source machine learning framework utilized to design and train sophisticated AI models. TensorFlow empowers the AI RC Car with neural networks capable of object recognition, decision-making, and autonomous navigation, ensuring adaptability in dynamic environments.

### **FileZilla**
A terminal emulator enabling seamless wireless connection to the Raspberry Pi via an online server. FileZilla facilitates file transferring from one device to another and remote access, offering flexibility and efficiency in development.

### **realVNC**
realVNC is a integral connection system that provided substantial progress for us by allowing us to connect wirelessly to the raspberry pi and control it on our computer. It offers much adpatability and leverage for our vehicle. 
---

## Key Components

### **Calibrate**
A pivotal process for optimizing sensor accuracy and motor precision. Calibration fine-tunes the hardware components to deliver reliable data and precise movements, ensuring seamless and consistent performance in varied conditions.

### **Config**
A centralized configuration system housing critical parameters, including sensor thresholds, motor speed limits, and neural network hyperparameters. This module simplifies system adjustments, enabling rapid optimization for diverse scenarios.

### **Manage**
A comprehensive management framework orchestrating the AI RC Car’s operations. It supervises system health, manages inter-component communication, and ensures synchronized functionality for smooth execution of autonomous tasks.

### **myconfig**
A customizable configuration file that stores user-defined preferences and specific environment settings. This personalization layer adapts the car’s behavior to unique challenges, enhancing flexibility and performance.

### **Train**
A sophisticated training module built on TensorFlow that iteratively refines AI models. It processes vast datasets, optimizes neural network parameters, and continuously evaluates performance, driving the evolution of the car’s autonomy and intelligence.

---

## Enhanced Workflow Process

### **1. Workflow Configuration**
The initial setup leverages the `config` and `myconfig` modules to tailor the car's system parameters and settings to the target environment, ensuring optimal readiness.

### **2. Calibration**
Sensors and motors undergo meticulous calibration to achieve maximum accuracy and responsiveness, forming the foundation for reliable and adaptive operation.

### **3. Training**
The AI models are trained using TensorFlow, iterating through data processing, model refinement, and performance evaluation to enhance decision-making and navigation capabilities.

### **4. Deployment**
With FileZilla, the refined control software is deployed to the Raspberry Pi, enabling remote updates and real-time software management.

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
* [PWM with ic2 interface](https://www.adafruit.com/product/815) - Mechanical controller 🤖
* [Li-Polymer Model 603048 (7.4V, 850mAh)](https://usa.banggood.com/ZOP-Power-7_4V-850mAh-100C-2S-LiPo-Battery-XT30-Plug-for-RC-Drone-p-1978448.html?utm_source=googleshopping&utm_medium=cpc_organic&gmcCountry=US&utm_content=minha&utm_campaign=aceng-pmax-usg-pc&currency=USD&cur_warehouse=CN&createTmp=1) - Powers the RC car 🔋
* [HYD001 Portable Charger](https://manuals.plus/miady/miady-hyd001-power-bank-user-manual) - Powers the raspberry pi and rest of the sensors 🪫






