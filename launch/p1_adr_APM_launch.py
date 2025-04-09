#!/usr/bin/env python3

import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Nodo publisher
        Node(
            package='p1_adr_APM',           # Nombre del paquete
            executable='publisher',    # Nombre del nodo ejecutable
            name='publisher',               # Nombre del nodo en ROS
            output='screen',                # Redirigir la salida al terminal
        ),
        
        # Nodo subscriber
        Node(
            package='p1_adr_APM',           # Nombre del paquete
            executable='subscriber',   # Nombre del nodo ejecutable
            name='subscriber',              # Nombre del nodo en ROS
            output='screen',                # Redirigir la salida al terminal
        ),
    ])
