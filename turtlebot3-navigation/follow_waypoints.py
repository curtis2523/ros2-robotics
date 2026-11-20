#! /usr/bin/env python3
# Copyright 2021 Samsung Research America
# Adapted during coursework with an office-map initial pose and nine waypoints.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration

"""
Basic navigation demo to go to poses.
"""


def main():
    rclpy.init()

    navigator = BasicNavigator()

    # Set our demo's initial pose
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x = 10.715829849243164
    initial_pose.pose.position.y = 2.823676586151123
    initial_pose.pose.orientation.z = -0.6921783958823713
    initial_pose.pose.orientation.w = 0.7217264497534417
    navigator.setInitialPose(initial_pose)

    # Activate navigation, if not autostarted. This should be called after setInitialPose()
    # or this will initialize at the origin of the map and update the costmap with bogus readings.
    # If autostart, you should `waitUntilNav2Active()` instead.
    # navigator.lifecycleStartup()

    # Wait for navigation to fully activate, since autostarting nav2
    navigator.waitUntilNav2Active()

    # set our demo's goal poses to follow
    goal_poses = []

    goal_pose1 = PoseStamped()
    goal_pose1.header.frame_id = 'map'
    goal_pose1.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose1.pose.position.x = 10.715829849243164
    goal_pose1.pose.position.y = 2.823676586151123
    goal_pose1.pose.orientation.w = 0.707
    goal_pose1.pose.orientation.z = 0.707
    goal_poses.append(goal_pose1)

    goal_pose2 = PoseStamped()
    goal_pose2.header.frame_id = 'map'
    goal_pose2.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose2.pose.position.x = 10.875655174255371
    goal_pose2.pose.position.y = -0.23122981190681458
    goal_pose2.pose.orientation.w = 0.707
    goal_pose2.pose.orientation.z = 0.707
    goal_poses.append(goal_pose2)

    goal_pose3 = PoseStamped()
    goal_pose3.header.frame_id = 'map'
    goal_pose3.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose3.pose.position.x = 8.46290397644043
    goal_pose3.pose.position.y = -0.3211413025856018
    goal_pose3.pose.orientation.w = 0.707
    goal_pose3.pose.orientation.z = 0.707
    goal_poses.append(goal_pose3)

    goal_pose4 = PoseStamped()
    goal_pose4.header.frame_id = 'map'
    goal_pose4.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose4.pose.position.x = 6.9866838455200195
    goal_pose4.pose.position.y = -0.35416102409362793
    goal_pose4.pose.orientation.w = 0.707
    goal_pose4.pose.orientation.z = 0.707
    goal_poses.append(goal_pose4)

    goal_pose5 = PoseStamped()
    goal_pose5.header.frame_id = 'map'
    goal_pose5.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose5.pose.position.x = 6.60673713684082
    goal_pose5.pose.position.y = 2.1697375774383545
    goal_pose5.pose.orientation.w = 0.707
    goal_pose5.pose.orientation.z = 0.707
    goal_poses.append(goal_pose5)

    goal_pose6 = PoseStamped()
    goal_pose6.header.frame_id = 'map'
    goal_pose6.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose6.pose.position.x = 6.647585391998291
    goal_pose6.pose.position.y = -0.2408445179462433
    goal_pose6.pose.orientation.w = 0.707
    goal_pose6.pose.orientation.z = 0.707
    goal_poses.append(goal_pose6)

    goal_pose7 = PoseStamped()
    goal_pose7.header.frame_id = 'map'
    goal_pose7.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose7.pose.position.x = 5.414508819580078
    goal_pose7.pose.position.y = -0.3337777853012085
    goal_pose7.pose.orientation.w = 0.707
    goal_pose7.pose.orientation.z = 0.707
    goal_poses.append(goal_pose7)

    goal_pose8 = PoseStamped()
    goal_pose8.header.frame_id = 'map'
    goal_pose8.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose8.pose.position.x = 5.464038848876953
    goal_pose8.pose.position.y = -2.548109292984009
    goal_pose8.pose.orientation.w = 0.707
    goal_pose8.pose.orientation.z = 0.707
    goal_poses.append(goal_pose8)


    goal_pose9 = PoseStamped()
    goal_pose9.header.frame_id = 'map'
    goal_pose9.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose9.pose.position.x = 5.717565059661865
    goal_pose9.pose.position.y = -0.15054842829704285
    goal_pose9.pose.orientation.w = 0.707
    goal_pose9.pose.orientation.z = 0.707
    goal_poses.append(goal_pose9)


    nav_start = navigator.get_clock().now()
    navigator.followWaypoints(goal_poses)

    i = 0
    while not navigator.isTaskComplete():
        ################################################
        #
        # Implement some code here for your application!
        #
        ################################################

        # Do something with the feedback
        i = i + 1
        feedback = navigator.getFeedback()
        if feedback and i % 5 == 0:
            print('Executing current waypoint: ' +
                  str(feedback.current_waypoint + 1) + '/' + str(len(goal_poses)))
            now = navigator.get_clock().now()

            # Some navigation timeout to demo cancellation
            if now - nav_start > Duration(seconds=600.0):
                navigator.cancelTask()

            # Some follow waypoints request change to demo preemption
            if now - nav_start > Duration(seconds=1000.0):
                goal_pose9 = PoseStamped()
                goal_pose9.header.frame_id = 'map'
                goal_pose9.header.stamp = now.to_msg()
                goal_pose9.pose.position.x = 5.717565059661865
                goal_pose9.pose.position.y = -0.15054842829704285
                goal_pose9.pose.orientation.w = 0.707
                goal_pose9.pose.orientation.z = 0.707
                goal_poses = [goal_pose9]
                nav_start = now
                navigator.followWaypoints(goal_poses)

    # Do something depending on the return code
    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('Goal succeeded!')
    elif result == TaskResult.CANCELED:
        print('Goal was canceled!')
    elif result == TaskResult.FAILED:
        print('Goal failed!')
    else:
        print('Goal has an invalid return status!')

    navigator.lifecycleShutdown()

    exit(0)


if __name__ == '__main__':
    main()
