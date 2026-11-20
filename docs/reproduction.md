# Source Layout

| Path | Contents |
| --- | --- |
| [custom-robot](../custom-robot) | Standalone URDF, ament package, Gazebo Classic and RViz2 launch files, and RViz config from the custom robot exercise |
| [turtlebot3-navigation/follow_waypoints.py](../turtlebot3-navigation/follow_waypoints.py) | Nav2 Simple Commander example adapted during the course with a starting pose and nine map-frame poses |
| [turtlebot3-navigation/maps](../turtlebot3-navigation/maps) | The Week 5 occupancy grid and its relative map configuration |
| [turtlebot3-navigation/course-config](../turtlebot3-navigation/course-config) | Selected office mapping and navigation launch files, SDF spawning helper, navigation parameters and referenced course map variants |

The original workspaces used ROS 2 Humble and Gazebo Classic. The office launch files refer to course package and scene assets; the source snapshot does not bundle the full original office model or generated workspace. The office launch variant and the Week 5 waypoint script refer to different map files. Check the [evidence map](evidence-map.md) for the source of each file.

The original rosbag database remains in the local archive. Its recorded streams include transforms, odometry, map, localization, scan and velocity data. The declared waypoint channel contains zero recorded messages. The waypoint coordinates are in the Python script. Release preparation was limited to organizing and reviewing the artifacts.
