Key Performance Indicators (KPI) for Integration Test
========================================================
The integration tests verify the proper interaction and data flow between critical ROS nodes. As a result, each test checks that multiple components are working together as intended.

Structural Risk Assessment and Map Building
----------------------------------------------
This integration test verifies the proper interaction between the key components developed in the Structural Risk Assessment task. Specifically, it checks that:

- A **damage detection message** is correctly published when damage is identified.
- A **map message** is correctly generated and published during the environment mapping process.

The test runs within a ROS environment where necessary sensor data are simulated using rosbags. After its execution, the following KPI might be implemented:

A possible integration KPI could be the **Total Response Time <= 2 s**, where the time between the sensor reading and the alert sent to the operator is measured. Performing the test, we obtained a success rate of 100% and an average total response lower than two seconds.

Victim detection and Triage
---------------------------------

This integration test is designed to validate the interaction between two critical tasks of the system: **victim detection** and **triage reporting**. Specifically, it ensures that once the victim detection module successfully detects a victim, an alarm is sent to the operator with relevant information and the victim triage is performed. 

A performable KPI of this test could be the **Total Response Time <= 10 s**, where we measure the time between the person identification and the triage alert sent to the operator.