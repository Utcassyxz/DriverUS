# AI RC Car Schematic Diagram

```mermaid
flowchart TD
    %% Power Sources
    PB["🔋 Portable Battery<br><sub>Power for Raspberry Pi</sub>"] --> RPI["🖥️ Raspberry Pi<br><sub>Central Processor</sub>"]
    CB["🔋 Car Battery<br><sub>Power for Motors</sub>"] --> MC["⚙️ Motor Control<br><sub>Controls Motors</sub>"]

    %% Raspberry Pi Connections
    RPI -->|Data| S1["📡 Sensor 1<br><sub>Obstacle Detection</sub>"]
    RPI -->|Data| S2["📡 Sensor 2<br><sub>Line Tracking</sub>"]
    RPI -->|PWM Signal| PWM["🎛️ PWM<br><sub>Pulse Width Modulation</sub>"]

    %% PWM and Motor Connections
    PWM --> MC
    MC --> M1["🛞 Motor 1"]
    MC --> M2["🛞 Motor 2"]

    %% Additional Connections
    CB --> MC
    %% Direct connection from car battery to motor control
