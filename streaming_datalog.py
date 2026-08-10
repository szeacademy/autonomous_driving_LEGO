from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Button
from pybricks.tools import wait, StopWatch

LEFT_MOTOR_PORT = Port.B
RIGHT_MOTOR_PORT = Port.F
LEFT_DIR = -1 
RIGHT_DIR = 1
WHEEL_CIRCUMFERENCE_MM = 176      #change according to wheel size
SAMPLE_MS = 5

hub = PrimeHub()
left_motor = Motor(LEFT_MOTOR_PORT)
right_motor = Motor(RIGHT_MOTOR_PORT)


def distance_mm(left_deg, right_deg):
    avg = (abs(left_deg) + abs(right_deg)) // 2
    return (avg * WHEEL_CIRCUMFERENCE_MM) // 360


def gyro_angle():
    h = hub.imu.heading()
    return int(h - 360 if h > 180 else h)


hub.display.char("S")

while True:
    if Button.RIGHT in hub.buttons.pressed():
        while Button.RIGHT in hub.buttons.pressed():
            wait(20)

        hub.imu.reset_heading(0)
        wait(100)
        left_motor.reset_angle(0)
        right_motor.reset_angle(0)
        wait(50)

        watch = StopWatch()

        hub.display.char("R")
        wait(200)

        print("plot: start :distance,gyro_angle")
        print("plot:0,0")

        while True:
            left_deg = left_motor.angle() * LEFT_DIR
            right_deg = right_motor.angle() * RIGHT_DIR
            d = distance_mm(left_deg, right_deg)
            g = gyro_angle()
            #print("plot:%d,%d,%d" % (watch.time(), d, g))
            print("plot:%d,%d" % ( d, g))

            if Button.RIGHT in hub.buttons.pressed():
                while Button.RIGHT in hub.buttons.pressed():
                    wait(20)
                break

            wait(SAMPLE_MS)

        hub.display.char("1")

    wait(50)