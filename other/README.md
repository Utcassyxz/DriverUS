Other Information
====

Located in this file is all the miscellaneous componenets of our vehicle creation process that didn't fit in the other cateogries. 

**Working Progress**

Located in this folder is images/videos and descriptions of our team recording data, training data, debugging, building, designing, and programming throughout the course of the project.  

**Design Process/Prototypes**
picamera, wheels, screen, bumper cut, lego top model three times, battery design, minor lego structure fixes/fixing wires, raspberry pi, camera cable

**Design 1:**

Our first model consisted of a simple lego structure on top of a drifting RC car (not our final RC car). A picture of the lego portion is attached below:
![image](https://github.com/user-attachments/assets/3e4bb468-0319-4018-863d-a683a51c2b06)

**Design 2:**

Although the drift car was fast a major problem that we encountered with the prototype was that 

# Model training efficiency
A feature that was included when we were training our data using Tensorflow was data loss while training. In the beginning we were using around 8000 pieces of data per model. The training loss graph is displayed below:
![mypilot (1)](https://github.com/user-attachments/assets/e1064463-4a4f-4767-b06b-b817a59de9d6)

We can see that the training loses around 8.5% of data throughout the training process. We improved this later on by training only around 5000 data pieces per model. The training loss graph is shown below:
![mypilot](https://github.com/user-attachments/assets/14fde4a8-b973-40da-8f83-1cd77651b252)

Where we can see that on average 5% of data is lost. Thus in the end we decided to use around 5000 pieces of data which maximized the training efficiency of our data. 

**Design Timeline**

# Visual Timeline

```mermaid
gantt
    title Project Timeline
    dateFormat  MM-YYYY
    section Planning
    Initial Brainstorming         :a1, 05-01-2024, 14d
    Initial Consturction of Vehicle    :a2, after a1, 21d
    section Development/Designing
    Software Development     :b1, 06-01-2024, 35d
    Debugging/Reserach         :b2, after b1, 21d
    section Training Model/Github
    Started GitHub       :c1, 07-01-2024, 90d
    Training AI model    :c2, after b2, 100d
    section Finalization
    Testing and Integration  :d1, 11-01-2024, 21d
    Prepare for Turkey       :d2, after d1, 2d
