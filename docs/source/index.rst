.. Cogar Assignments documentation master file, created by
   sphinx-quickstart on Thu Apr  3 10:45:37 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cogar Assignments documentation
===============================

This repository contains the code for the `Assignment_Cogar` project.  

Repository Structure
--------------------
# TODO: write the repository structure once finisher

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


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   component_diagram
   behaviour_diagram
   integration_KPI

