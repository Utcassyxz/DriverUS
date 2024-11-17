```mermaid
flowchart TD
    RPI[Raspberry Pi] -->|PWM Signal| MD[Motor Driver]
    MD --> M1[Motor 1]
    MD --> M2[Motor 2]
    RPI -->|Data| S1[Sensor 1]
    RPI -->|Data| S2[Sensor 2]
    PS[Power Supply] --> RPI
    PS --> MD
