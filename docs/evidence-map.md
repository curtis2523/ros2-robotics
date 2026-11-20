# Evidence Map

## Source key

B2, B3, B5 and B7 refer to the student report DOCX files in 机电一体化 / Weeks 2, 3, 5 and 7. The private manifest keeps the original filenames. Page numbers use local PDF renders. The saved Week 5 and 7 workspace setup scripts identify the Humble underlay.

| Claim | Source | Evidence |
| --- | --- | --- |
| ROS 2 foundational lab | B2 and Week 2 packages | Publisher and subscriber exercise outside the featured modules |
| Gazebo, RViz2 and TurtleBot3 Waffle | B3 pp. 2–6 and B5 p. 1 | Startup, laser visualization, teleoperation and office simulation |
| SLAM Toolbox and occupancy grid | B3 pp. 4–8, 10 and Week 5 maps directory | Async mapping, repeat passes, slower coverage and successful export after correcting the flag |
| Course office launch variants | B3 pp. 9–10 and officev4_mapping.py / officev4_navigation.py | Separate launch paths. The navigation variant uses my_map3.yaml, while the Week 5 waypoint exercise specifies the Week 5 export |
| AMCL and Nav2 | B5 pp. 1–2, 4 | Goal arrival, localization and costmap feedback |
| Python route customization | B5 pp. 2–4 and Week 5 waypoint script | Nav2 Simple Commander example adapted with office-map initial pose and nine waypoints |
| rosbag2 capture and replay | B5 pp. 3–5 and Week 5 metadata.yaml and SQLite bag | Recorded messages and qualitative playback. The database establishes actual per-topic counts |
| Custom URDF and bringup | B7 pp. 1–5 and curtis251_bringup | Separate package, geometry, joints, spawn and RViz launch |
| Drive and sensors | B7 pp. 4–6 and URDF plugin blocks | Differential drive, odometry, camera, IMU and LiDAR configuration |
| Custom robot troubleshooting | B7 p. 6 | Reported corrections to wheel drive, materials and sensor placement |
