Behaviour diagram
======================

.. The Behavioral Diagram and its description for each mandatory component. The choice of behavioral diagram should be consistent with the type of component.

Structural Risk Assessment
-------------------------------

A state diagram was chosen to fully represent this task. This type of behavioral diagram allows us to clearly model how the different components are connected and exchange information as the robot's state changes — from the initial configuration where the robot is simply powered on, to assessing the nearby environment, and finally to exploring the map until it is fully covered. Once the exploration is successfully completed, a success signal is sent. Each state is associated with specific actions and conditions that define how the robot navigates and responds to its environment.

Looking in more detail, the diagram highlights how this task can be logically divided into four main parts:

- **Approach**: Typically triggered after Risk Assessment if the information retrieved from the sensors is not sufficient to perform a wall evaluation. In this phase, the robot moves closer to better assess the structure.
- **Risk Assessment**: After gathering sensor data, the system performs crack detection on the structure (referred to simply as "wall"). If cracks are found, a damage evaluation follows (Damage Detection). Lastly, if the information is sufficient, the wall is classified according to its risk level.
- **Danger Reporting**: If the wall classification identifies a dangerous structure, the position of the critical wall is computed and a report about the detected criticality is generated and sent.
- **Exploration**: The robot continues the 3D mapping of the environment, plans its next moves based on current data, and executes movement tasks.

This sequence is repeated iteratively until the environment is fully explored.

.. #TODO: in the behavior diagram do we have to add wall_detection before crack detection?
 #TODO: do we have to implement the planning block?
 #TODO: remove emergency button or implement it in the code? Remove error handling?

# TODO: ADD THE DIAGRAM HERE

Victim detection and Reporting
-------------------------------

something

Triage system
----------------------


.. .. image:: img/behavioural_diagram-task3.png
    :alt: Task 3 behavioral diagram