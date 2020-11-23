import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(16, True)

GPIO.output(22, False)
GPIO.output(36, False)
GPIO.output(37, False)

p = GPIO.PWM(16, 5000)

def SpinMotor(direction, num_steps):
    p.ChangeFrequency(5000)
    GPIO.output(18, direction)
    while num_steps > 0:
        p.start(1)
        time.sleep(0.01)
        num_steps -= 1
    p.stop()
    return True

if __name__ == '__main__':

    dir_in = input('0 cw 1 ccw 3 size: ')

    while(dir_in):
        dir = int(dir_in)

        if (dir == 1) or (dir == 0):
            num_in = input('num steps: ')
            num = int(num_in)
            SpinMotor(dir, num)

        elif dir == 3:
            GPIO.output(36, False)
            GPIO.output(37, True)

        dir_in = input('0 cw 1 ccw 3 size: ')

    GPIO.cleanup()
