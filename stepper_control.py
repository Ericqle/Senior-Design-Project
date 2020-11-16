
import RPi.GPIO as GPIO, time

# Single Stepper Motor Control
# TODO finish implementation, add variable speed/ timing
"""
    Pins are rasberry pi GPIO pins connected to driver for specific motor.
    Easy driver IO: 
        step:       increment motor one step (variable size) 
        direction:  cw/ccw control
        ms1:        logic input for step size
        ms2:        logic input for step size
"""
class StepperControl:
    pin_step = 0
    pin_direction =0
    ##pin_ms1 = 0
    ##pin_ms2 = 0
    p = None

    # stepper driver init
    def __init__(self, pin_step, pin_direction):
        # set pins
        self.pin_step = pin_step
        self.pin_direction = pin_direction
        ##self.pin_ms1 = pin_ms1
        ##self.pin_ms2 = pin_ms2

        # init driver
        GPIO.setup(self.pin_step, GPIO.OUT)
        GPIO.setup(self.pin_direction, GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.output(self.pin_step, True)
        self.p = GPIO.PWM(self.pin_step, 5000)

    # spin cw/ccw with fixed amount of steps
    def spin_fixed_step(self, direction, num_steps):
        self.p.ChangeFrequency(5000)
        GPIO.output(self.pin_direction, direction)
        while num_steps > 0:
            self.p.start(1)
            time.sleep(0.01)
            num_steps -= 1
        self.p.stop()
        GPIO.cleanup()
        return True

    # TODO spin cw/ccw with fixed amount of full/half/quarter/eigth steps
    """
    Map type_step to:
    MS1         MS2         Step Type
    0           0           Full
    0           1           Half
    1           0           Quarter
    1           1           Eight    
    """
    def spin_fixed_step_type(self, direction, num_steps, type_step):
        print("TODO")