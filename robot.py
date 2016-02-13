#!/usr/bin/env python3

import wpilib
import time
from mechanisms import *

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.joystick_right = wpilib.Joystick(0)
        self.joystick_left = wpilib.Joystick(1)

        self.motor_left = wpilib.Jaguar(0)
        self.motor_right = wpilib.Jaguar(1)

        self.motor_shooter_left = wpilib.Jaguar(2)
        self.motor_shooter_right = wpilib.Jaguar(3)
        self.motor_shooter_lift = wpilib.Jaguar(4)
        self.motor_shooter_release = wpilib.Jaguar(5)

        self.shooter = Shooter.Shooter(left_motor=self.motor_shooter_left, right_motor=self.motor_shooter_right, tilt_motor=self.motor_shooter_lift, release_motor=self.motor_shooter_release)

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

        # Control the tilt of the shooter
        if self.joystick_right.getRawButton(3):
            self.shooter.tilt_up()
        elif self.joystick_right.getRawButton(4):
            self.shooter.tilt_down()
        else:
            self.shooter.stop_tilt()

        # Control the launch wheels
        if self.joystick_right.getRawButton(5):
            self.shooter.receive_boulder()
        elif self.joystick_right.getRawButton(6):
            self.shooter.set_boulder_speed(1.0)
        else:
            self.shooter.stop_launcher()

        # The kick should be either in receive position or kicking the boulder
        if self.joystick_right.getRawButton(7):
            self.shooter.kick_boulder()
        else:
            self.shooter.open_release()

if __name__ == '__main__':
    wpilib.run(MyRobot)
