import RPi.GPIO as GPIO
from plotter.draw_control import DrawControl

if __name__ == '__main__':
    zotter = DrawControl()

    test = input("track, rail, pen, hor ")

    while(test):
        if(test == "track"):
            dir_in = input('0 cw 1  ccw: ')
            num_in = input('num steps: ')
            dir = int(dir_in)
            num = int(num_in)

            if dir_in:
                zotter.track.spin_fixed_step(dir, num)
                print(dir, "", num)
            else:
                zotter.track.spin_fixed_step(dir, num)
                print(dir, "", num)

        elif(test == "rail"):
            dir_in = input('0 cw 1  ccw: ')
            num_in = input('num steps: ')
            dir = int(dir_in)
            num = int(num_in)

            if dir_in:
                zotter.rail.spin_fixed_step(dir, num)
                print(dir, "", num)
            else:
                zotter.rail.spin_fixed_step(dir, num)
                print(dir, "", num)

        elif(test == "servo"):
            angle = float(input("angle: "))
            zotter.pen_holder.turn_angle(angle)

        elif(test == "hor"):
            zotter.draw_hor_line(0, 200)

        test = input("track, rail, pen, hor ")

        zotter.close_board()