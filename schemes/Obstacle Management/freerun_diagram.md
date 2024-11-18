# Schematic Diagram: AI-Powered Lap Detection System

```mermaid
flowchart TD
    A[Initialize Pi Camera] --> B[Load Trained TensorFlow Model]
    B --> C[Start Capturing Frames Continuously]
    C --> D[Capture Frame from Camera]
    D --> E[Process Frame using TensorFlow Model]
    E --> F{Has Gyroscope Detected 3 Laps?}
    F -- Yes --> G[Stop the Code]
    F -- No --> D
