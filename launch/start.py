"""Launch Hesai ROS2 driver with config passed as parameter."""

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    """Generate launch description."""
    share_dir = get_package_share_directory('hesai_ros_driver')
    rviz_config = os.path.join(share_dir, 'rviz', 'rviz2.rviz')
    config_path = os.path.join(share_dir, 'config', 'config.yaml')
    with open(config_path, 'r') as f:
        config_yaml = f.read()

    return LaunchDescription([
        Node(
            namespace='hesai_ros_driver',
            package='hesai_ros_driver',
            executable='hesai_ros_driver_node',
            output='screen',
            parameters=[{'config_yaml': config_yaml}],
        ),
        Node(
            namespace='rviz2',
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config],
        ),
    ])
