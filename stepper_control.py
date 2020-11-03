
import RPi.GPIO as GPIO, time

# Single Stepper Motor Control
class StepperControl:
    step_pin = 0
    direction_pin =0
    ms1_pin = 0
    ms2_pin = 0
    p = GPIO.PWM(step_pin, 5000)

    # stepper driver init
    def stepper_control(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.setup(self.direction_pin, GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.output(self.step_pin, True)

    # spin cw/ccw with fixed amount of steps
    def spin_fixed_step(self, direction, num_steps):
        self.p.ChangeFrequency(5000)
        GPIO.output(self.direction_pin, direction)
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
    def spin_fixed_step(self, direction, num_steps, type_step):
        print("TODO")