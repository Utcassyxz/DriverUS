# Enhanced Horizontal Flowchart with Color

```mermaid
flowchart LR
    style A fill:#FFDDC1,stroke:#E67E22,stroke-width:2
    style B fill:#FFABE1,stroke:#E91E63,stroke-width:2
    style C fill:#B5EAD7,stroke:#27AE60,stroke-width:2
    style D fill:#C9CBE9,stroke:#2980B9,stroke-width:2
    style E fill:#F5F5DC,stroke:#8E44AD,stroke-width:2
    style K fill:#F8C471,stroke:#D35400,stroke-width:2
    style F fill:#FFE4E1,stroke:#C0392B,stroke-width:2
    style G fill:#D5F5E3,stroke:#1ABC9C,stroke-width:2

    A([📷 Initialize Pi Camera]) --> B([🧠 Load Trained TensorFlow Model])
    B --> C([🎥 Start Capturing Frames Continuously])
    C --> D([📸 Capture Frame from Camera])
    D --> E([⚙️ Process Frame using TensorFlow Model])
    E --> K([🚙 Adjust Throttle and Steering of the Vehicle Accordingly])
    K --> F{🏁 Has Gyroscope Detected 3 Laps?}
    F -- Yes --> G([🛑 Stop the Code])
    F -- No --> D
