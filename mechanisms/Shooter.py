import wpilib

class Shooter:
    def __init__(self, left_motor, right_motor, tilt_motor, release_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.tilt_motor = tilt_motor
        self.release_motor = release_motor

    def set_boulder_speed(self, motor_speed):
        self.left_motor.set(motor_speed)
        self.right_motor.set(-motor_speed)

    def set_lift_speed(self, motor_speed):
        self.lift_motor.set(motor_speed)

    def receive_boulder(self):
        self.release_motor.set(-1.0)
        self.set_boulder_speed(-0.75)

    def open_release(self):
        self.release_motor.set(-1.0)

    def tilt_up(self):
        self.tilt_motor.set(1.0)

    def tilt_down(self):
        self.tilt_motor.set(-1.0)

    def stop_tilt(self):
        self.tilt_motor.set(0.0)

    def kick_boulder(self):
        self.release_motor.set(1.0)

    def stop_launcher(self):
        self.set_boulder_speed(0.0)
