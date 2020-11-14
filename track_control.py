from stepper_control import StepperControl

"""
    Implementation of track movement. At the moment only focusing on movement for a fixed number
    of steps before any further implementation.
"""

class TrackControl:

    stepper_motor_track = None

    def __init__(self, pin_step, pin_direction, pin_ms1, pin_ms2):
        # init stepper motor
        self.stepper_motor_track = StepperControl(pin_step, pin_direction, pin_ms1, pin_ms2)

    def move_fixed(self, dir, num_steps):
        self.stepper_motor_track.spin_fixed_step(dir, num_steps)
