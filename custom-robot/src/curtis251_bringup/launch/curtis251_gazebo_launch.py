from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    # === 获取路径 ===
    pkg_share = get_package_share_directory('curtis251_bringup')
    urdf_file = os.path.join(pkg_share, 'urdf', 'curtis251_robot.urdf')

    # 检查 URDF 是否存在
    assert os.path.exists(urdf_file), f"URDF file not found: {urdf_file}"

    # === 1) 启动 Gazebo (Classic) 空世界 ===
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        ),
        launch_arguments={'verbose': 'true'}.items()
    )

    # === 2) 发布 /robot_description 给 Gazebo 和 RViz 用 ===
    robot_state_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': open(urdf_file).read(),
            'use_sim_time': True
        }]
    )

    joint_state_pub = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen'
    )

    # === 4) 在 Gazebo 中生成机器人实体 ===
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_curtis251_bot',
        output='screen',
        arguments=[
            '-entity', 'curtis251_bot',
            '-topic', 'robot_description',
            '-x', '0', '-y', '0', '-z', '0.04'   # 离地 2cm 防止坠落侧翻
        ]
    )

    # === 5) 返回 LaunchDescription ===
    return LaunchDescription([
        gazebo,
        robot_state_pub,
        joint_state_pub,
        spawn_entity
    ])
