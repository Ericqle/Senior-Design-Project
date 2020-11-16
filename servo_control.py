import RPi.GPIO as GPIO
import time

class ServoControl:
    pin_signal = 0;

    def __init__(self, pin_signal):
        self.pin_signal = pin_signal
        GPIO.setup(self.pin_signal,GPIO.OUT)
        self.servo = GPIO.PWM(self.pin_signal, 50)

    def turn_angle(self, angle):
        self.servo.start(0)
        self.servo.ChangeDutyCycle(2 + (angle / 18))
        time.sleep(0.5)
        self.servo.ChangeDutyCycle(0)
        self.servo.stop()
        GPIO.cleanup()

