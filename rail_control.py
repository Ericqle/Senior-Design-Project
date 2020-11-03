from stepper_control import StepperControl

"""
    Implementation of top rail movement. At the moment only focusing on movement for a fixed number
    of steps before any further implementation.
"""

class RailControl:

    stepper_motor_rail = None

    def RailControl(self, pin_step, pin_direction, pin_ms1, pin_ms2):
        # init stepper motor
        self.stepper_motor_rail = StepperControl(pin_step, pin_direction, pin_ms1, pin_ms2)

    def move_up_down(self, num_steps):
        self.stepper_motor_rail.spin_fixed_step(dir, num_steps)
