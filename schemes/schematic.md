```mermaid
flowchart TD
    RPI["🖥️ Raspberry Pi<br><sub>Central Processor</sub>"] -->|PWM Signal| MD["⚙️ Motor Driver<br><sub>Controls Motors</sub>"]
    MD --> M1["🛞 Motor 1"]
    MD --> M2["🛞 Motor 2"]
    RPI -->|Data| S1["📡 Sensor 1<br><sub>Obstacle Detection</sub>"]
    RPI -->|Data| S2["📡 Sensor 2<br><sub>Line Tracking</sub>"]
    PS["🔋 Power Supply"] --> RPI
    PS --> MD
