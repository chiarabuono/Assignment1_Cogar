.. Cogar Assignments documentation master file, created by
   sphinx-quickstart on Thu Apr  3 10:45:37 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cogar Assignments documentation
================================

This repository contains the code for the `Assignment_Cogar` project.

Group Members
-----------------------

- Roberto Bertelli s728918@studenti.unige.it
- Chiara Buono s7687956@studenti.unige.it
- Mattia Tinfena s7852527@studenti.unige.it

Link github repository: https://github.com/chiarabuono/Assignment1_Cogar

Requirements
--------------

Before installing Python packages, you must install the following dependencies:

.. code-block:: bash

    sudo apt install ros-${ROS_DISTRO}-audio-common-msgs

where {ROS_DISTRO} is the ROS distribution installed on your system. After system dependencies are installed, install Python packages:

.. code-block:: bash

    pip install -r requirements.txt

Repository Structure
--------------------

Repo's tree::

  +- docs
    |  +- build
    |  |  +- doctrees
    |  |  +- html
    |  +- make.bat
    |  +- Makefile
    |  +- requirements.txt
    |  +- source
    |     +- behavioural_diagram.rst
    |     +- component_diagram.rst
    |     +- conf.py
    |     +- custom_messages.rst
    |     +- img
    |     |  +- behavioural_diagram-task1.drawio.png
    |     |  +- behavioural_diagram-task2.drawio.png
    |     |  +- behavioural_diagram-task3.drawio.png
    |     |  +- component_diagram.drawio.png
    |     +- index.rst
    |     +- integration_KPI.rst
    |     +- interface_description.rst
    |     +- unit_KPI.rst
    +- README.md
    +- src
       +- assignments
       |  +- bags
       |  |  +- arm_jointstate.bag
       |  |  +- depth_raw.bag
       |  |  +- force_sensor.bag
       |  |  +- odometry.bag
       |  |  +- rgb_raw.bag
       |  |  +- scan_lidar.bag
       |  |  +- sonar.bag
       |  +- CMakeLists.txt
       |  +- launch
       |  |  +- task.launch
       |  +- msg
       |  |  +- Crack.msg
       |  |  +- Cracks.msg
       |  |  +- Map.msg
       |  |  +- Velocities.msg
       |  |  +- Wall.msg
       |  +- package.xml
       |  +- src
       |  |  +- arm_motion_service.py
       |  |  +- closer_inspection.py
       |  |  +- crack_detection.py
       |  |  +- damage_detection.py
       |  |  +- localization.py
       |  |  +- map_builder.py
       |  |  +- message_sender.py
       |  |  +- microphone.py
       |  |  +- person_alert.py
       |  |  +- speaker_service.py
       |  |  +- trajectory_control.py
       |  |  +- victim_detection.py
       |  |  +- victim_triage.py
       |  |  +- wall_identification.py
       |  +- srv
       |  |  +- Alert.srv
       |  |  +- CheckJointState.srv
       |  |  +- CloserInspection.srv
       |  |  +- DamageReport.srv
       |  |  +- Destination.srv
       |  |  +- Speaker.srv
       |  |  +- TriageReport.srv
       |  |  +- VictimReport.srv
       |  |  +- WallStatus.srv
       |  +- tests
       |     +- task1_integration_test.py
       |     +- task1_integration_test.test
       |     +- task2_3_integration_test.py
       |     +- task2_3_integration_test.test
       +- CMakeLists.txt -> /opt/ros/noetic/share/catkin/cmake/toplevel.cmake

.. - **src/**
  Contains the `assignments` ROS package, which includes Python service nodes.
  All services are presented together, but they are organized by assignments as follows:
  - **Topic 1 Services:**
    - `speaker_service.py`
 - **srv/**
  Contains all custom ROS service definitions, categorized per topics:
  - **Topic 1 .srv:**
    - `Speaker.srv`
 - **docs/**
  Includes documentation materials and reference content used to write this documentation.

- **TIAGo .bag**

  Below are the data collected in bags from the TIAGo sensors, which can be found on OneDrive.
  Each bag represents inputs captured from one specific sensor, including:

  - RGB-D Camera: Depth raw images, RGB raw images.
  - LiDAR: Environment point cloud.
  - SONAR: Distance measurements.
  - Force Sensors: Force and Torque measurementsof the right arm.
  - Odometry: Provides the robot's current position and velocity.
  - Arm Joint State: Includes information about the robot's limb, such as positions, velocities, and effort. 

  In order to be able to run the integration tests correctly, it is necessary to download these bags and place them inside a folder called "bags" in the assignments folder: /src/assignments/bags.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   component_diagram
   behavioural_diagram
   interface_description
   custom_messages
   unit_KPI
   integration_KPI
   
