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
 - In: 
    - geometry_msgs/Point position

 - Out: 
    - bool received

.. _DamageReport:

DamageReport
------------
- In:
    - geometry_msgs/Point position
    - string severity

- Out:
    - bool received

.. _Destination:

Destination
----------------
- In:
    - geometry_msgs/Point destination
    
- Out:
    - bool received

.. _Speaker:

Speaker
----------------
- In:
    - string message
    
- Out:
    - bool success

.. _TriageReport:

TriageReport
----------------
- In:
    - geometry_msgs/Point position
    - int64 severity
    
- Out:
    - bool received

.. _VictimReport:

VictimReport
----------------
- In:
    - geometry_msgs/Point position
    
- Out:
    - bool received