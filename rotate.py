from __future__ import division
from threading import Thread
import time
import Adafruit_PCA9685
import sys
from multiprocessing import Process
pwm = Adafruit_PCA9685.PCA9685()
servo_min = 150
servo_max = 600


def rotate(channel, angle):
    cent = angle/100
    pulse = int(375*cent)+servo_min
    pwm.set_pwm(channel, 0, pulse)
    time.sleep(0.1)
    if channel == 2:
        pwm.set_pwm(channel, 0, pulse+5)
        time.sleep(0.1)
        pwm.set_pwm(channel, 0, pulse-5)
    time.sleep(1)


if __name__ == '__main__':
    pwm.set_pwm_freq(60)
    arg = sys.argv
    if len(arg) < 4:
        sys.exit("failed")
    p1 = Process(target=rotate, args=(1, int(arg[1])))
    p1.start()
    p2 = Process(target=rotate, args=(2, int(arg[2])))
    p2.start()
    p3 = Process(target=rotate, args=(3, int(arg[3])))
    p3.start()
    p4 = Process(target=rotate, args=(0, int(arg[4])))
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print("success")

