# Flowchart for Obstacle Avoidance and Parking Logic
([🐢 Slow Down and Align to Park])
([🛑 Stop When Parked])

```mermaid
flowchart TB
    %% Define styles for better visualization
    style A fill:#1ABC9C,stroke:#148F77,stroke-width:2,color:#FFFFFF
    style B fill:#3498DB,stroke:#2E86C1,stroke-width:2,color:#FFFFFF
    style C fill:#E67E22,stroke:#D35400,stroke-width:2,color:#FFFFFF
    style D fill:#9B59B6,stroke:#76448A,stroke-width:2,color:#FFFFFF
    style E fill:#F1C40F,stroke:#D4AC0D,stroke-width:2,color:#000000
    style F fill:#E74C3C,stroke:#CB4335,stroke-width:2,color:#FFFFFF
    style G fill:#2ECC71,stroke:#27AE60,stroke-width:2,color:#FFFFFF
    style H fill:#34495E,stroke:#2C3E50,stroke-width:2,color:#FFFFFF
    style I fill:#7F8C8D,stroke:#5D6D7E,stroke-width:2,color:#FFFFFF

    %% Nodes
    A([📷 Initialize Pi Camera]) --> B([🧠 Load Trained TensorFlow Model])
    B --> C([🎥 Start Capturing Frames Continuously])
    C --> D{🔄 While True}
    D --> E([📸 Capture Frame from Camera])
    E --> F([⚙️ Process Frame using TensorFlow Model])
    F --> G([🧭 Monitor Gyroscope to Track Laps])
    
    %% Obstacle Detection Branch
    G --> H{🚧 Obstacle Detected?}
    H -- Yes --> I([📏 Calculate Distance and Direction])
    I --> J([➡️ Determine Left or Right Maneuver])
    J --> K([⚙️ Adjust Steering and Throttle to Avoid Obstacle])
    H -- No --> L([➡️ Continue Along Default Path])

    %% Turning/not turning Branch
    K --> M{🧭 Gyro detects over 2 laps?}
    L --> M
    M -- No --> D
    M -- Yes --> N([❔ Red or Green detected?])
    N -- Red 🔴 --> O([Turn vehicle around and set model as `opposte`])
    N -- Green 🟢 --> P([Continue moving forward and set model as `foward`])
    O --> Q([Continue driving the card in the designated direction while dodging obstacles])
    P --> Q
    Q --> R([🧭 Gyro detects another lap?)
    R -- No and model is `opposite` --> O
    R -- No and model is `forward` --> P
    R -- Yes --> S([Initialize parking model])




