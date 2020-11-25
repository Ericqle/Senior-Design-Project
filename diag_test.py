import RPi.GPIO as GPIO, time
import threading

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(16, True)
GPIO.output(13, True)
p = GPIO.PWM(16, 5000)
p2 = GPIO.PWM(13, 5000)


def SpinMotor1(direction, num_steps, delay, freq):
    p.ChangeFrequency(freq)
    GPIO.output(18, direction)
    while num_steps > 0:
        p.start(1)
        time.sleep(delay)
        num_steps -= 1
    p.stop()
    return True


def SpinMotor2(direction, num_steps, delay ,freq):
    p2.ChangeFrequency(freq)
    GPIO.output(15, direction)
    while num_steps > 0:
        p2.start(1)
        time.sleep(delay)
        num_steps -= 1
    p2.stop()
    return True


def SpinMotor12( dir1, dir2, num_steps1, num_steps2):
    delay1 = 0.01
    delay2 = 0.01
    freq1 = 5000
    freq2 = 5000

    if num_steps1 > num_steps2:
        time = delay1 * num_steps1
        delay2 = float("{:.4f}".format(time / num_steps2))
        freq2 = (freq2 / (num_steps1/num_steps2))
        freq2 = float("{:.4f}".format(freq2))
    elif num_steps2 > num_steps1:
        time = delay2 * num_steps2
        delay1 = float("{:.4f}".format(time / num_steps1))
        freq1 = (freq1 / (num_steps2 / num_steps1))
        freq1 = float("{:.4f}".format(freq1))

    print(str(dir1) + " " + str(num_steps1) + " " + str(delay1) + " " + str(freq1))
    print(str(dir2) + " " + str(num_steps2) + " " + str(delay2) + " " + str(freq2))

    t1 = threading.Thread(target=SpinMotor1, args=(dir1, num_steps1, delay1, freq1))
    t2 = threading.Thread(target=SpinMotor2, args=(dir2, num_steps2, delay2, freq2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()



if __name__ == '__main__':

    dir_in = input('dir1 dir2 steps1 steps2: ')

    while dir_in:
        dir = dir_in.split(" ")
        SpinMotor12(int(dir[0]), int(dir[1]), int(dir[2]), int(dir[3]))
        dir_in = input('dir1 dir2 steps1 steps2: ')

    GPIO.cleanup()
