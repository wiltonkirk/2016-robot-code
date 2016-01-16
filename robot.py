#!/usr/bin/env python3

import wpilib
import time

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.joystick_right = wpilib.Joystick(0)
        self.joystick_left = wpilib.Joystick(1)

        self.motor_left = wpilib.Jaguar(0)
        self.motor_right = wpilib.Jaguar(1)

        self.drive_train = wpilib.RobotDrive(self.motor_left, self.motor_right)
        self.drive_train.setExpiration(0.2)

    def autonomousInit(self):
        # Motors have to be updated every 0.2 seconds or they stop - disable
        # that in autonomous mode
        self.drive_train.setSafetyEnabled(False)

        # Re-enable the motor watchdog timer when we're done
        self.drive_train.setSafetyEnabled(True)

    def teleopPeriodic(self):
        self.drive_train.arcadeDrive(self.joystick_right.getY(), self.joystick_left.getX() * -1)

        # Right Arm Motor
        # if self.joystick_right.getRawButton(3):
        #     self.motor_right_arm.set(0.65)
        # elif self.joystick_right.getRawButton(4):
        #     self.motor_right_arm.set(-0.65)
        # else:
        #     self.motor_right_arm.set(0.0)



if __name__ == '__main__':
    wpilib.run(MyRobot)
