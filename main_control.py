from stepper_control import StepperControl
import RPi.GPIO as GPIO

# Pi pins
TRACK_PIN_STEP = 16
TRACK_PIN_DIRECTION = 18
#TRACK_PIN_MS1 = 0
#TRACK_PIN_MS2 = 0
RAIL_PIN_STEP = 0
RAIL_PIN_DIRECTION =0
#RAIL_PIN_MS1 = 0
#RAIL_PIN_MS2 = 0

# Primary full-board draw functions
"""
    Primary source for drawing control. Implements the usage of StepperControl and ServoControl
    functions to draw an Image.

"""
class DrawControl:
    track = None
    rail = None

    def __init__(self):
        # Init Board
        GPIO.setmode(GPIO.BOARD)

        # Init Steppers and Servos
        self.track = StepperControl(TRACK_PIN_STEP, TRACK_PIN_DIRECTION)
        #self.rail = StepperControl(RAIL_PIN_STEP, RAIL_PIN_DIRECTION, RAIL_PIN_MS1, RAIL_PIN_MS2)

if __name__ == '__main__':
    zotter = DrawControl()

    dir_in = input('0 cw 1  ccw')
    num_in = input('num steps')
    dir = int(dir_in)
    num = int(num_in)
    if dir_in:
        zotter.track.spin_fixed_step(dir, num)
        print(dir, "", num)
    else:
        zotter.track.spin_fixed_step(dir, num)
        print(dir, "", num)
