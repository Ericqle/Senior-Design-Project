# sample code from
# https://raspberryautomation.com/control-a-steppermotor-with-a-raspberry-pi/

import RPi.GPIO as GPIO, time;

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(16, True)

p = GPIO.PWM(16, 5000)

def SpinMotor(direction, num_steps):
    p.ChangeFrequency(5000)
    GPIO.output(18, direction)
    while num_steps > 0:
        p.start(1)
        time.sleep(0.01)
        num_steps -= 1
    p.stop()
    GPIO.cleanup()
    return True
