# RoboticArm
Arm made for doing transactions at fuel dispenser.

Servo Details:
channel 0 = rotating base servo
channel 1 = main arm servo at base
channel 2 = mid arm servo
channel 3 = small servo at fingers to hold card

Generic command to rotate arm:
python rotate.py 50 50 100 50
                 |  |   |   |
Channels         1  2   3   0

The above generic command will set setvos and arm to a right angle 90° ready to swipe card position

For safety reasons (python rotate.py 50 0 100 50) is considered as resting position of arm and this position decreased the stress on servos

PHP:
In localnetwork
ip/index.php?motor1=50&motor2=50&motor3=100&motor4=50

motors sequence is same in both python and php commands
