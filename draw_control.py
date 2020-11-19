from stepper_control import StepperControl
from servo_control import ServoControl
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
        self.track = StepperControl(TRACK_PIN_STEP, TRACK_PIN_DIRECTION)
        self.rail = StepperControl(RAIL_PIN_STEP, RAIL_PIN_DIRECTION)
        self.pen_holder = ServoControl(SERVO_PIN_SIGNAL)

        # Start servo for pen holder max height
        self.pen_holder.turn_angle(120)

    def close_board(self):
        self.pen_holder.servo.stop()
        GPIO.cleanup()

    def draw_hor_line(self, dir, step):
        self.pen_holder.turn_angle(45)
        self.track.spin_fixed_step(dir, step)
        self.pen_holder.turn_angle(120)

    def draw_ver_line(self, dir, step):
        self.pen_holder.turn_angle(45)
        self.rail.spin_fixed_step(dir, step)
        self.pen_holder.turn_angle(120)

    def draw_square(self, step):
        self.pen_holder.turn_angle(45)
        self.rail.spin_fixed_step(0, step)
        self.track.spin_fixed_step(0, step)
        self.rail.spin_fixed_step(1, step)
        self.track.spin_fixed_step(1, step)
        self.pen_holder.turn_angle(120)