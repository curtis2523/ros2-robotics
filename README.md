# ROS 2 Robot Simulation & Navigation

![ROS 2 Robotics cover using the original custom robot capture](assets/cover.webp)

## Project Overview

Two undergraduate Mechatronics exercises. In the first, I modeled a custom differential-drive robot with sensor plugins and built a Gazebo and RViz2 bringup package. In the second, I used a TurtleBot3 Waffle to map a simulated office, navigate through waypoints and record ROS topics for replay.

## My Role & Contributions

I authored the custom robot URDF, configured its wheels, caster and sensor mounts, and wrote launch files and package configuration. For TurtleBot3, I drove the mapping passes, exported the occupancy grid, recorded goal poses in RViz2 and adapted a Nav2 Simple Commander example with an initial pose and nine waypoints. I also recorded and replayed the navigation session.

## Tech Stack

| Practice | Tools |
| --- | --- |
| Custom robot | ROS 2 Humble, ament_python, Python launch, URDF, Gazebo Classic, RViz2 |
| TurtleBot3 | TurtleBot3 Waffle, Gazebo Classic, RViz2, SLAM Toolbox, Nav2, AMCL, Python and Nav2 Simple Commander |
| Session recording | rosbag2 and SQLite |

## System Architecture

```mermaid
flowchart LR
    subgraph Custom["Custom robot bringup"]
        U["URDF and Python launch"] --> G["Gazebo Classic plugins"]
        U --> R["Robot state publisher and RViz2"]
        C["cmd_vel"] --> G
        G --> S["Camera, IMU, laser scan and odometry"]
    end
    subgraph Turtle["TurtleBot3 Waffle exercise"]
        T["Gazebo office and TurtleBot3"] --> M["SLAM Toolbox"]
        M --> O["Saved occupancy grid"]
        O --> N["Nav2 and AMCL"]
        W["Python waypoint client"] --> N
        N --> T
        T --> B["rosbag2 topic recording"]
        N --> B
        B --> V["Topic playback and RViz2 inspection"]
    end
```

## Implementation

- **Custom robot.** A cylindrical base, two wheels on continuous joints and a fixed caster form the chassis. The URDF defines sensor frames and Gazebo plugins for differential drive, camera, IMU and LiDAR. Separate launch files cover Gazebo spawning and standalone RViz2 inspection.
- **TurtleBot3.** I used teleoperation and asynchronous SLAM to build the map. I checked a single goal in RViz2, then passed nine map-frame poses to Nav2's waypoint follower. The bag preserves TF, odometry, localization, map, scan and velocity messages.

## Challenges & Solutions

The custom robot report describes correcting wheel joint references and drive parameters, adding Gazebo-compatible materials and adjusting sensor placement. Initial office mapping attempts showed gaps or drift. Slowing down and covering rooms deliberately produced the saved map, and correcting the map-saver output flag to `-f` produced the PGM/YAML pair. I then iterated on the waypoint sequence and tested playback.

## Project Screenshots

| Course evidence | Original capture |
| --- | --- |
| Custom robot in Gazebo | ![Custom robot and laser scan](assets/screenshots/custom-robot-gazebo.png) |
| TurtleBot3 in the office | ![Office simulation with TurtleBot3 LiDAR](assets/screenshots/turtlebot3-office-gazebo.png) |
| Completed occupancy grid | ![Office occupancy grid in RViz2](assets/screenshots/turtlebot3-rviz-slam.png) |
| Navigation and costmaps | ![RViz2 navigation map](assets/screenshots/turtlebot3-rviz-navigation.png) |
| Session replay | ![Gazebo and RViz2 during playback](assets/screenshots/turtlebot3-bag-replay.png) |

## Original Course Recordings

- Custom robot · [Gazebo bringup](assets/demos/custom-robot-gazebo-bringup.mp4) and [RViz2 model inspection](assets/demos/custom-robot-rviz-model-inspection.mp4)
- TurtleBot3 · [Office waypoint navigation](assets/demos/turtlebot3-office-waypoint-navigation.mp4) and [rosbag playback](assets/demos/turtlebot3-rosbag-playback.mp4)

See the [video index](docs/video-index.md) for provenance and edits.

## Results & Limitations

The course records show a spawned custom robot, a saved occupancy grid, a goal reached in RViz2 and a waypoint run through three rooms. Playback republishes messages, while reproducing simulated motion depends on the running nodes and simulator state. The submissions provide qualitative simulation evidence. The recordings are from the original coursework.

## Course Source

The [custom robot package](custom-robot) and [TurtleBot3 navigation artifacts](turtlebot3-navigation) belong to separate exercises. See the [source layout](docs/reproduction.md) for the retained files and course environment dependencies.

## Course Project Background

ITFM7.120 Mechatronics in IT. Week 3 covers mapping, Week 5 covers TurtleBot3 navigation and replay, and Week 7 covers custom robot modeling and bringup.

[Evidence map](docs/evidence-map.md) · [Image index](docs/image-index.md) · [Portfolio copy](PORTFOLIO.md) · [Credits](docs/credits.md) · [Publication checklist](PUBLISH-CHECKLIST.md)
