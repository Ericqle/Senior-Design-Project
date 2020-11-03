from stepper_control import StepperControl

class RailControl:

    stepper_motor_rail = None

    def RailControl(self, pin_step, pin_direction, pin_ms1, pin_ms2):
        # init stepper motor
        self.stepper_motor_rail = StepperControl(pin_step, pin_direction, pin_ms1, pin_ms2)

    def move_up(self):
        print("TODO")

    def move_down(self):
        print("TODO")
