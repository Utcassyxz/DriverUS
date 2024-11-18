# Software and AI Modeling Flowchart

```mermaid
flowchart TD
    %% Software Section
    A[Start: RC Car Software] --> B[Load manage.py]
    B --> C[Manual Control & Data Recording]
    C --> H[Sort & Manage Data]

    %% Transition to AI Modeling
    H --> I[Start: AI Modeling Process]
    I --> J[Collect Data with Joystick]
    J --> K[Store Data on Raspberry Pi]
    K --> L[Transfer Data to PC with FileZilla]
    L --> M[Organize Files in MyCar Folder]
    M --> N[Train AI Model with TensorFlow]
    N --> O[Export Model to Raspberry Pi]
    O --> P[Integrate Model with airc_drive10.py]
    P --> Q[AI Model Ready for Autonomous Driving]
