# Modify the target-angle equation to match your equation

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=62.4, axle_track=120)#dm56 without big wheels
robot.reset()
hub.imu.reset_heading(0) 
proportional_gain = 6  


def ad_navigation(equation,distance,R2,direction,fast_speed,slow_speed):



        while (robot.distance() < distance and direction == 1) or (robot.distance() > distance and direction == -1): # Drive for mm
                # 1. Convert mm to cm to prevent numbers from blowing up
                x = robot.distance() / 1.0

                # 2. Run polynomial math equation route 
                # Put the equation here - -0.318 + 0.0213x + -1.28E-05x^2 + -5.39E-08x^3 + 8.66E-11x^4 + -3.54E-14x^5
                #target_angle = -4.68 + -0.0871*x + 1.72E-03*x**2 + -4.64E-06*x**3 + 4.23E-09*x**4 + -1.25E-12*x**5
                target_angle = equation(x)
                fit_R2 = R2  # Assuming a perfect fit for simplicity

                # Add this in if you just want to drive straight during these distances
                if x <= 0:
                    target_angle = 0.0  # Drive straight at the beginning and end of the path
                    base_speed = slow_speed*direction
                elif x >= distance - 1:
                   #target_angle = 0.0  # Drive straight at the beginning and end of the path
                    base_speed = slow_speed*direction
                else:
                    target_angle = target_angle * fit_R2  # Scale the target angle by the R² value to improve accuracy
                    base_speed = fast_speed*direction


                # 3. Calculate steering corrections
                current_angle = hub.imu.heading()
                error = target_angle - current_angle

                turn_rate = error * proportional_gain

                print(round(x,1), round(target_angle,1), round(current_angle,1), round(error,2), round(turn_rate,2),base_speed, sep=" |")

                robot.drive(base_speed, turn_rate)

                wait(10)

try:
    equation = lambda x: INSERTEQUATIONHERE
    distance = INSERTDISTANCEHERE
    R2 = INSERTR2HERE
    ad_navigation(equation, distance, R2,1)
    robot.stop()
    wait(2000)
        
finally:
    robot.stop()
