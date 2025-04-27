Custom messages
===============

Crack
-----
 - geometry_msgs/Point position 
 - std_msgs/String severity

.. _Cracks:

Cracks
------
 - uint32 n_cracks 
 - Crack[] cracks

.. _Map:

Map
---
 - Wall[] walls
 - geometry_msgs/Point[] victims 
 - bool completed

.. _Velocities:

Velocities
----------
 - float64[4] velocities

.. _Wall:

Wall
----
 - geometry_msgs/Point position
 - float64 height
 - float64 width

Custom services
===============

.. _CloserInspection:

CloserInspection
----------------
 - Request: 
    - geometry_msgs/Point position

 - Response: 
    - bool received

.. _DamageReport:

DamageReport
------------
- Request:
    - geometry_msgs/Point position
    - string severity

- Response:
    - bool received

.. _Destination:

Destination
----------------
- Request:
    - geometry_msgs/Point destination
    
- Response:
    - bool received

.. _Speaker:

Speaker
----------------
- Request:
    - string message
    
- Response:
    - bool success

.. _TriageReport:

TriageReport
----------------
- Request:
    - geometry_msgs/Point position
    - int64 severity
    
- Response:
    - bool received

.. _VictimReport:

VictimReport
----------------
- Request:
    - geometry_msgs/Point position
    
- Response:
    - bool received