import wpilib

class Shooter:
    def __init__(self, left_motor, right_motor, tilt_motor, kick_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.tilt_motor = tilt_motor
        self.kick_motor = kick_motor

    def set_boulder_speed(self, motor_speed):
        self.left_motor.set(motor_speed)
        self.right_motor.set(-motor_speed)

    def set_lift_speed(self, motor_speed):
        self.lift_motor.set(motor_speed)

    def stop_kick(self):
        self.kick_motor.set(0.0)

    def tilt_up(self):
        self.tilt_motor.set(1.0)

    def tilt_down(self):
        self.tilt_motor.set(-1.0)

    def stop_tilt(self):
        self.tilt_motor.set(0.0)

    def run_kick(self):
        self.kick_motor.set(-1.0)

    def stop_launcher(self):
        self.set_boulder_speed(0.0)
