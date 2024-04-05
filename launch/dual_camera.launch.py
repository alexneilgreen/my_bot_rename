import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():



    front_camera_spawner = Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            output='screen',
            parameters=[{
                'image_size': [640,480],
                'camera_frame_id': 'front_camera_link_optical'
                }]
    )

    rear_camera_spawner = Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            output='screen',
            parameters=[{
                'image_size': [640,480],
                'camera_frame_id': 'rear_camera_link_optical'
                }]
    )

    return LaunchDescription([

        front_camera_spawner,
        rear_camera_spawner

    ])
