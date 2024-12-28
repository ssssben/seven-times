import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    number = launch_ros.actions.Node(
        package = 'mypkg',
        executable = 'number',
    )
    answer = launch_ros.actions.Node(
        package = 'mypkg',
        executable = 'answer',
        output = 'screen',
    )

    return launch.LaunchDescription([number, answer])
