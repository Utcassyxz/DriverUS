# Enhanced Horizontal Flowchart with Improved Contrast

```mermaid
flowchart TB
    style A fill:#E67E22,stroke:#D35400,stroke-width:2,color:#FFFFFF
    style B fill:#E91E63,stroke:#C2185B,stroke-width:2,color:#FFFFFF
    style C fill:#27AE60,stroke:#1E8449,stroke-width:2,color:#FFFFFF
    style D fill:#2980B9,stroke:#1A5276,stroke-width:2,color:#FFFFFF
    style E fill:#8E44AD,stroke:#6C3483,stroke-width:2,color:#FFFFFF
    style K fill:#D35400,stroke:#A04000,stroke-width:2,color:#FFFFFF
    style F fill:#C0392B,stroke:#922B21,stroke-width:2,color:#FFFFFF
    style G fill:#1ABC9C,stroke:#148F77,stroke-width:2,color:#FFFFFF

    A([📷 Initialize Pi Camera]) --> B([🧠 Load Trained TensorFlow Model])
    B --> C([🎥 Start Capturing Frames Continuously])
    C --> D([📸 Capture Frame from Camera])
    D --> E([⚙️ Process Frame using TensorFlow Model])
    E --> K([🚙 Adjust Throttle and Steering of the Vehicle Accordingly])
    K --> F{🏁 Has Gyroscope Detected 3 Laps?}
    F -- Yes --> G([🛑 Stop the Code])
    F -- No --> D
