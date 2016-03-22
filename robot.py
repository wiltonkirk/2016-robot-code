#!/usr/bin/env python3

import wpilib
import time
from mechanisms import *

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.kicking = False

        self.joystick_drive = wpilib.Joystick(0)
        self.joystick_lift = wpilib.Joystick(1)

        self.motor_left = wpilib.Jaguar(0)
        self.motor_right = wpilib.Jaguar(1)

        self.motor_shooter_left = wpilib.Talon(4)
        self.motor_shooter_right = wpilib.Talon(5)
        self.motor_shooter_lift = wpilib.Jaguar(2)
        self.motor_shooter_kick = wpilib.Jaguar(3)

        self.kick_stop = wpilib.DigitalInput(2)
        self.soft_lift_stop = wpilib.DigitalInput(1)

        self.shooter = Shooter.Shooter(left_motor=self.motor_shooter_left,
                                       right_motor=self.motor_shooter_right,
                                       tilt_motor=self.motor_shooter_lift,
                                       kick_motor=self.motor_shooter_kick)
        self.drive_train = wpilib.RobotDrive(self.motor_left, self.motor_right)


        self.elbow_motor = wpilib.Jaguar(6)
        self.arm_tilt = wpilib.Jaguar(7)

        self.autonomous_picker = wpilib.AnalogInput(0)

        self.drive_train.setExpiration(0.2)

    def autonomousInit(self):
        self.drive_train.drive(0.0, 0.0)

        # Motors have to be updated every 0.2 seconds or they stop - disable
        # that in autonomous mode
        self.drive_train.setSafetyEnabled(False)

        self.shooter.tilt_down()
        time.sleep(1.1)
        self.shooter.stop_tilt()

        if self.autonomous_picker.getVoltage() < 1.66:
            self.drive_train.drive(0.40, -0.05)
            time.sleep(1.1)
            self.drive_train.drive(0.0, 0.0)

        elif self.autonomous_picker.getVoltage() < 3.34:
            self.drive_train.drive(0.40, -0.05)
            time.sleep(1.932)
            self.drive_train.drive(0.0, 0.0)

        else:
            self.drive_train.drive(0.65, 0.0)
            time.sleep(1.5)
            self.drive_train.drive(0.0, 0.0)

        # Re-enable the motor watchdog timer when we're done
        self.drive_train.setSafetyEnabled(True)

    def autonomousPeriodic(self):
        self.drive_train.drive(0.0, 0.0)
        if not self.kick_stop.get():
            self.shooter.run_kick()
        else:
            self.shooter.stop_kick()

    def teleopInit(self):
        self.kicking = False
        self.shooter.stop_kick()

    def teleopPeriodic(self):
         # Switch to tank drive if a special button is held down
        if self.joystick_drive.getRawButton(8) or self.joystick_drive.getRawButton(6):
            self.drive_train.tankDrive(self.joystick_drive.getY(), self.joystick_drive.getAxis(4))
        else:
            self.drive_train.arcadeDrive(self.joystick_drive.getY(), self.joystick_drive.getZ())

        # Control the tilt of the shooter
        if self.joystick_lift.getRawButton(4) and not self.soft_lift_stop.get():
            self.shooter.tilt_up()
        elif self.joystick_lift.getRawButton(2):
            self.shooter.tilt_down()
        elif self.joystick_lift.getRawButton(4) and self.joystick_lift.getRawButton(9):
            self.shooter.tilt_up()
        else:
            self.shooter.stop_tilt()

        # Control the launch wheels
        if self.joystick_lift.getRawButton(1):
            self.shooter.set_boulder_speed(-0.4)
        elif self.joystick_lift.getRawButton(3):
            if self.joystick_lift.getRawButton(8):
                self.shooter.set_boulder_speed(0.5)
            else:
                self.shooter.set_boulder_speed(0.85)
        else:
            self.shooter.stop_launcher()

        #
        # kick_stop = not self.kick_stop.get()
        # # Set a flag that we should complete a rotation so we don't stop
        # # until we've gotten all the way around
        # if self.joystick_lift.getRawButton(7): # Set the flag and start rotation
        #     self.kicking = True
        #     self.shooter.run_kick()
        # elif self.kicking and kick_stop: # If we're kicking and we haven't moved enough to
        #     self.shooter.run_kick()                 # flip the switch, run anyway
        # elif self.kicking and not kick_stop: # After the switch is depressed, unset the flag
        #     self.shooter.run_kick()                     # and keep going
        #     self.kicking = False
        # else: # If we have no idea whats going on stop everything
        #     self.shooter.stop_kick()

        if self.joystick_lift.getRawButton(7):
            self.shooter.run_kick()
        else:
            self.shooter.stop_kick()


if __name__ == '__main__':
    wpilib.run(MyRobot)
