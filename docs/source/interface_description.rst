Interface description
=====================

- **/xtion/rgb/image_raw**
    - Message type: sensor_msgs/Image
    - State: Stateless
    - Data/Service: Data
    - Strongly/loosely - typed: Strongly typed

- **/scan**
    - Message type: sensor_msgs/LaserScan 
    - State: Stateless
    - Data/Service: Data
    - Strongly/loosely - typed: Strongly typed

- **/mobile_base_controller/odom**
    - Message type: nav_msgs/Odometry
    - State: Stateless
    - Data/Service: Data
    - Strongly/loosely - typed: Strongly typed

- **/sonar_base**
    - Message type: sensor_msgs/Range
    - State: Stateless
    - Data/Service: Data
    - Strongly/loosely - typed: Strongly typed

- **map**
    - Message type: :ref:`Map`
    - State: Stateful
    - Data/Service: Data
    - Strongly/loosely - typed: Strongly typed

- **localization**
    - Message type: geometry_msgs/Point
    - State: Stateless
    - Data/Service: Data
    - Strongly/loosely - typed: Strongly typed

- **walls**
    - Message type: :ref:`Wall`
    - State: Stateless
    - Data/Service: Data
    - Strongly/loosely - typed: Strongly typed

- **cracks**
    - Message type: :ref:`Cracks`

    - State: Stateless
    - Data/Service: Data
    - Strongly/loosely - typed: Strongly typed

- **movement_destination**
    - Message type: :ref:`Destination`

    - State: Stateless
    - Data/Service: Service
    - Strongly/loosely - typed: Strongly typed

- **demage_message**
    - Message type: :ref:`DamageReport`

    - State: Stateless
    - Data/Service: Service
    - Strongly/loosely - typed: Strongly typed

- **speaker**
    - Message type: :ref:`Speaker`

    - State: Stateless
    - Data/Service: Service
    - Strongly/loosely - typed: Strongly typed

- **mic**
    - Message type: audio_common_msgs/AudioData
    - State: Stateless
    - Data/Service: Data
    - Strongly/loosely - typed: Strongly typed

- **victim_detected**
    - Message type: geometry_msgs/Point
    - State: Stateless
    - Data/Service: Data
    - Strongly/loosely - typed: Strongly typed

- **victim_detection_message**
    - Message type: :ref:`VictimReport`

    - State: Stateless
    - Data/Service: Service
    - Strongly/loosely - typed: Strongly typed

- **triage_message**
    - Message type: :ref:`TriageReport`

    - State: Stateless
    - Data/Service: Service
    - Strongly/loosely - typed: Strongly typed

- **closer_inspection**
    - Message type:  :ref:`CloserInspection`

    - State: Stateless
    - Data/Service: Service
    - Strongly/loosely - typed: Strongly typed

- **motor_velocities**
    - Message type: :ref:`Velocities`

    - State: Stateless
    - Data/Service: Data
    - Strongly/loosely - typed: Strongly typed