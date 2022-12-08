import os

import launch
import launch_ros.actions

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    lidarcameracalib_param_dir = launch.substitutions.LaunchConfiguration(
        'lidarcameracalib_param_dir',
        default=os.path.join(get_package_share_directory('lidar_camera_calib'),
            'config',
            'calib.yaml'))

    lidarcameracalib = launch_ros.actions.Node(
        package='lidar_camera_calib',
        executable='lidar_camera_calib',
        name='lidar_camera_calib',
        parameters=[os.path.join(get_package_share_directory('lidar_camera_calib'),
            'config',
            'calib.yaml')],
        output='screen'
        )


    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'lidarcameracalib_param_dir',
            default_value=lidarcameracalib_param_dir,
            description='Full path to lidarcameracalib parameter file to load'),
        lidarcameracalib,
            ])