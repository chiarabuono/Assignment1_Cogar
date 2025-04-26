Component diagram
===================

.. The architecture component diagram with accurate description detailing where different design patters could play a role in the final architecture implementation.
 #TODO in each file, not here
 For each component list:
 -  their interfaces 
 -  describe them according to the component-based  software architecture paradigm (i.e., stateless/statefull, data/service, strongly-typed/loosely-typed, etc).

This page provides an architectural component diagram. It is organizedinto three main subsystems:

- Structural Risk Assessment
- Victim Detection and Reporting
- Triage System

.. .. image:: /img/{absolut-document-subdirectory}/{file}.svg
  :alt: Alt text. Every image should have descriptive alt text.

Structural Risk Assessment
-------------------------------
This subsystem focuses on detecting cracks and unstable areas through image processing and sensor fusion. It also evaluate the overall building's risk level. It consists of two core subsystem: 3D mapping and Environment evaluation.

3D Mapping
^^^^^^^^^^^^^^
The 3D Mapping subsystem allows the robot to create a map the surrounding environment and determine its localization using information from its sensors. The map built enables the trajectory control component to function correctly, allowing the robot to autonomously plan and adapt its route in response to newly detected obstacles or debris. Once the environment is fully explored, the system notify the human supervisor and awaits further instructions. 

.. #TODO: implement integration test about the successfull receive of the ended mission

The 3D Mapping subsystem is strictly linked to the Environment evaluation subsystem. Specifically:

- The Map_Builder component provides the spatial map.
- The Localization component provides the robot's real-time position inside the given map.

These interfaces are highly important since once a critical structure is found by the Environment subsystem, it can be uploaded into the map, allowing the future operator to have a broader vision of the environment conditions.

.. # TODO: integration testing about Autonomous navigation: the robot adjusts its route based on newly detected obstacles, debris, or structural changes. It gives information to the trajectory control block

Sensor inputs are external to the system scope and are provided via ROS bag files. These include:

- RGB-D Camera
- LiDAR
- Sonar
- Odometry

Environment evaluation
^^^^^^^^^^^^^^^^^^^^^^^^
The environment evalutation subsystem uses the outputs from 3D Mapping to perform structural analysis. It comprises three component:

- Wall_Identification: Detects and categorizes walls and structural elements.
- Crack_Detection: Identifies fractures in structures and assesses their severity.
- Damage_Detection: Aggregates data to evaluate the overall structural integrity.

.. #TODO: Link to the corresponding message definition file.

When a weak wall with cracks is detected, the subsystem (and specifically tje Damage_Detection block) generates a real-time critical report and sends it to the human supervisor. Based on this report, the  supervisor can manually ask to a more detailed inspection of that precise spot. If required, the robot can autonomously approach the area for a more precise assessment.

.. # TODO: Did we implement the remote supervisor can manually request for more detailed evaluation of specific points?
.. # TODO: Did we implement the autonomously movement of the robot?


Victim detection and Reporting
-------------------------------
This subsystem uses RGB-D Cameras and Microphones to autonomously detect potential victims. When a victim is located, their position is computed, and a real-time alert is immediately notified to human rescuers.

After that, a triage is performed on the victim using the triage system block.


Triage system
----------------------
Once a victim is detected, this subsystem evaluates their physical condition to support prioritization in rescue operations. Using sensor data (RGB-D Camera and Microphones), the system computes:

- Consciousness
- Responsiveness
- Severity of injuries

Message_Sender
----------------
All three subsystems interface with the Message_Sender component—a service responsible for relaying alerts to the human operator. The type of alert sent depends on the source subsystem:

- Structural environment alarm
- Victim detected alarm
- Triage assessment completed

.. # TODO link the 3 srv

