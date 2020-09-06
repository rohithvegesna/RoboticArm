<?php
$motor1 = $_GET['motor1'];
$motor2 = $_GET['motor2'];
$motor3 = $_GET['motor3'];
$output = shell_exec('sudo python rotate.py '.$motor1.' '.$motor2.' '.$motor3);
