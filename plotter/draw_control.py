from plotter.stepper_control import StepperControl
from plotter.servo_control import ServoControl
import RPi.GPIO as GPIO

# Pi pins
TRACK_PIN_STEP = 16
TRACK_PIN_DIRECTION = 18
#TRACK_PIN_MS1 = 0
#TRACK_PIN_MS2 = 0
RAIL_PIN_STEP = 13
RAIL_PIN_DIRECTION = 15
#RAIL_PIN_MS1 = 0
#RAIL_PIN_MS2 = 0
SERVO_PIN_SIGNAL = 11

# Primary full-board draw functions
"""
    Primary source for drawing control. Implements the usage of StepperControl and ServoControl
    functions to draw an Image.

"""
class DrawControl:
    track = None
    rail = None
    pen_holder = None

    def __init__(self):
        # Init Board
        GPIO.setmode(GPIO.BOARD)

        # Init Steppers and Servos
        self.track = StepperControl(16, 18)
        self.rail = StepperControl(13, 15)
        self.pen_holder = ServoControl(11)

        # Start servo for pen holder max height
        self.pen_holder.turn_angle(120)

    def close_board(self):
        self.pen_holder.servo.stop()
        GPIO.cleanup()

    def draw_hor_line(self, dir, step):
        self.pen_holder.turn_angle(80)
        self.track.spin_fixed_step(dir, step)
        self.pen_holder.turn_angle(120)
