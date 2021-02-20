from stepper_control import StepperControl
from servo_control import ServoControl
import RPi.GPIO as GPIO
import threading

# Pi pins
TRACK_PIN_STEP = 16
TRACK_PIN_DIRECTION = 18
TRACK_PIN_MS1 = 36
TRACK_PIN_MS2 = 37
RAIL_PIN_STEP = 13
RAIL_PIN_DIRECTION = 15
RAIL_PIN_MS1 = 29
RAIL_PIN_MS2 = 31
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

    def pen_down(self):
        self.pen_holder.turn_angle(45)

    def pen_up(self):
        self.pen_holder.turn_angle(120)

    def draw_hor_line(self, dir, num_steps):
        self.track.spin_fixed_step(dir, num_steps)

    def draw_ver_line(self, dir, num_steps):
        self.rail.spin_fixed_step(dir, num_steps)

    # spin both motors with fixed amount of steps
    def draw_diagonal(self, dir1, dir2, num_steps1, num_steps2):
        delay1 = 0.05
        delay2 = 0.05
        freq1 = 600
        freq2 = 600

        if num_steps1 > num_steps2:
            time = delay1 * num_steps1
            delay2 = float("{:.10f}".format(time / num_steps2))
            freq2 = (freq2 / (num_steps1 / num_steps2))
            freq2 = float("{:.10f}".format(freq2))
        elif num_steps2 > num_steps1:
            time = delay2 * num_steps2
            delay1 = float("{:.10f}".format(time / num_steps1))
            freq1 = (freq1 / (num_steps2 / num_steps1))
            freq1 = float("{:.10f}".format(freq1))

        t1 = threading.Thread(target=self.track.spin_fixed_step_delay_freq, args=(dir1, num_steps1, delay1, freq1))
        t2 = threading.Thread(target=self.rail.spin_fixed_step_delay_freq, args=(dir2, num_steps2, delay2, freq2))

        t1.start()
        t2.start()

        t1.join()
        t2.join()


    def draw_diagonal2(self, dir1, dir2, num_steps1, num_steps2):
        delay1 = 0.01
        delay2 = 0.01
        freq1 = 5000.0
        freq2 = 5000.0
        num_steps1 = num_steps1
        num_steps2 = num_steps2

        if num_steps1 > num_steps2:
            freq2 = (freq2 * (num_steps2 / num_steps1))
            num_steps2 = num_steps1
        elif num_steps2 > num_steps1:
            freq1 = (freq1 * (num_steps2 / num_steps1))
            num_steps1 = num_steps2

        t1 = threading.Thread(target=self.track.spin_fixed_step_delay_freq2, args=(dir1, num_steps1, delay1, freq1))
        t2 = threading.Thread(target=self.rail.spin_fixed_step_delay_freq2, args=(dir2, num_steps2, delay2, freq2))

        t1.start()
        t2.start()

        t1.join()
        t2.join()
