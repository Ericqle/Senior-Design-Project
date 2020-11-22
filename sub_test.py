import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(16, True)

p = GPIO.PWM(16, 5000)
p.ChangeFrequency(5000)

def SpinMotor(direction, num_steps):
    GPIO.output(18, direction)
    while num_steps > 0:
        p.start(1)
        time.sleep(0.01)
        num_steps -= 1
    return True

def ChangeFreq(freq):
    p.ChangeFrequency(freq)

if __name__ == '__main__':

    dir_in = input('0 cw 1  ccw: ')

    while(dir_in):
        dir = int(dir_in)
        num_in = input('num steps: ')
        num = int(num_in)

        if (dir == 1) or (dir == 0):
            SpinMotor(dir, num)

        dir_in = input('0 cw 1  ccw: ')

    p.stop()
    GPIO.cleanup()
