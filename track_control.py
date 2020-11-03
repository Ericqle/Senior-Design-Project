from stepper_control import StepperControl

class TrackControl:

    stepper_motor_track = None

    def TrackControl(self, pin_step, pin_direction, pin_ms1, pin_ms2):
        # init stepper motor
        self.stepper_motor_track = StepperControl(pin_step, pin_direction, pin_ms1, pin_ms2)

    def move_left(self, dir, num_steps):
        self.stepper_motor_track.spin_fixed_step(dir, num_steps)

    def move_right(self, dir, num_steps):
        self.stepper_motor_track.spin_fixed_step(dir, num_steps)


