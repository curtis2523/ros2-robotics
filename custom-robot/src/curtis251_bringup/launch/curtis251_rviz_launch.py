import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('curtis251_bringup')
    default_model_path = os.path.join(pkg_share, 'urdf', 'curtis251_robot.urdf')
    default_rviz_config_path = os.path.join(pkg_share, 'rviz', 'curtis251.rviz')

    # 启动参数
    use_sim_time = LaunchConfiguration('use_sim_time')
    use_rviz_config = LaunchConfiguration('use_rviz_config')  # 是否加载 .rviz
    model_arg = LaunchConfiguration('model')
    rvizconfig_arg = LaunchConfiguration('rvizconfig')
    gui = LaunchConfiguration('gui')

    # 读取 URDF
    with open(default_model_path, 'r') as f:
        robot_description_content = f.read()

    # robot_state_publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description_content,
            'use_sim_time': use_sim_time
        }]
    )

    # joint_state_publisher / GUI
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        condition=UnlessCondition(gui),
        parameters=[{'use_sim_time': use_sim_time}]
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen',
        condition=IfCondition(gui)
    )

    # RViz：两种模式
    # A) 不加载配置（自由视图，与你朋友一致）
    rviz_node_no_cfg = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        condition=UnlessCondition(use_rviz_config)
    )

    # B) 加载配置（当你确实想用保存好的布局时再开）
    rviz_node_with_cfg = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rvizconfig_arg],
        parameters=[{'use_sim_time': use_sim_time}],
        condition=IfCondition(use_rviz_config)
    )

    return LaunchDescription([
        DeclareLaunchArgument('gui', default_value='True',
                              description='Enable joint_state_publisher_gui'),
        DeclareLaunchArgument('use_sim_time', default_value='false',
                              description='Use simulation clock'),
        DeclareLaunchArgument('model', default_value=default_model_path,
                              description='Absolute path to robot URDF'),
        DeclareLaunchArgument('rvizconfig', default_value=default_rviz_config_path,
                              description='Absolute path to RViz config'),
        DeclareLaunchArgument('use_rviz_config', default_value='false',
                              description='Load the RViz config file if true'),

        joint_state_publisher_node,
        joint_state_publisher_gui_node,
        robot_state_publisher_node,
        rviz_node_no_cfg,
        rviz_node_with_cfg
    ])

