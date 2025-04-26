Key Performance Indicators (KPI) for Unit Test
=====================================================

This section defines the Key Performance Indicators (KPIs) used to evaluate the core ROS nodes responsible for 
structural analysis, victim detection, and triage in a post-earthquake search and rescue scenario. 
Each KPI includes its success threshold for unit testing and performance benchmarking.

Structural Risk Assessment
--------------------------

- **Crack Detection Accuracy (%) - Threshold: > 85%**  
  Measures the percentage of structural cracks correctly identified using sensor data and image processing.

- **False Positive Rate (%) - Threshold: < 10%**  
  Represents the proportion of incorrectly identified cracks or instabilities.

- **Sensor Fusion Latency (ms) - Threshold: <  200 ms**  
  Time required to integrate data from RGB-D, LiDAR, and sonar sensors for a complete environmental scan.

- **Wall Classification Confidence Score (0-1) - Threshold: > 0.75**  
  Indicates the certainty with which the system assigns a structural risk level to a wall.

- **Assessment Response Time (ms) - Threshold: < 1000 ms**  
  Time elapsed between detecting a potential structural issue and generating a full evaluation.

Victim Detection and Reporting
------------------------------

- **Detection Accuracy (%) - Threshold: > 90%**  
  Indicates how accurately the system detects injured individuals based on RGB-D and audio data.

- **Localization Error (m) - Threshold: < 0.5 m**  
  Measures the positional error between the detected and actual location of a victim.

- **Detection Time (s) - Threshold: < 5 s**  
  Time from the initial sensing of a victim to successful detection confirmation.

- **False Negative Rate (%) - Threshold: < 5%**  
  The rate at which the system misses real victims.

Triage System
-------------

- **Triage Classification Accuracy (%) - Threshold: > 85%**  
  The accuracy with which the system categorizes a victim's condition.

- **Response Evaluation Time (s) - Threshold: < 3 s**  
  Time needed to evaluate the victim's state using visual and audio inputs.

- **Speech Recognition Confidence (%) - Threshold: > 80%**  
  Average confidence of the system in recognizing spoken responses.

- **Classification Latency (ms) - Threshold: < 2000 ms**  
  The delay between initiating an evaluation and outputting a triage classification.