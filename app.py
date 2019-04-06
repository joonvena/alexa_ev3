#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

motor_right = LargeMotor('outA')
motor_left = LargeMotor('outD')

motor_right.run_timed(time_sp=3000, speed_sp=-750)