from draw_control import DrawControl

if __name__ == '__main__':
    zotter = DrawControl()

    test = input("track, rail, pen, hor, ver, square, diag: ")

    while(test):
        if test == "track":
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

        elif test == "rail":
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

        elif test == "pen":
            angle = float(input("angle: "))
            zotter.pen_holder.turn_angle(angle)

        elif test == "hor":
            zotter.draw_hor_line(0, 100)

        elif test == "ver":
            zotter.draw_ver_line(0, 100)

        elif test == "square":
            zotter.draw_square(50)

        elif test == "diag":
            zotter.draw_diagonal(0,0,100,100)

        test = input("track, rail, pen, hor, ver, square, diag: ")

    zotter.close_board()