from setuptools import setup
from glob import glob
import os

package_name = 'curtis251_bringup'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.py')),
        ('share/' + package_name + '/urdf', glob('urdf/*.urdf')),
        ('share/' + package_name + '/rviz', glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Curtis',
    maintainer_email='maintainer@example.invalid',
    description='Curtis251 Robot bringup for Gazebo and RViz2',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [],
    },
)
