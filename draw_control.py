from stepper_control import StepperControl
from servo_control import ServoControl
import RPi.GPIO as GPIO
import threading

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

    # spin both motors with fixed amount of steps
    """
        Concurrency via threads. Motors reach destination based on constant time
        -of longer axis-; and delays are changed to reflect this
    """
    def draw_diagonal(self, dir1, dir2, num_steps1, num_steps2):
        self.pen_holder.turn_angle(45)

        delay1 = 0.01
        delay2 = 0.01

        if num_steps1 > num_steps2:
            time = delay1 * num_steps1
            delay2 = float("{:.4f}".format(time / num_steps2))
            print(delay2)
        elif num_steps2 > num_steps1:
            time = delay2 * num_steps2
            delay1 = float("{:.4f}".format(time / num_steps1))
            print(delay1)

        t1 = threading.Thread(target=self.track.spin_fixed_step_delay, args=(dir1, num_steps1, delay1))
        t2 = threading.Thread(target=self.rail.spin_fixed_step_delay, args=(dir2, num_steps2, delay2))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        self.pen_holder.turn_angle(120)