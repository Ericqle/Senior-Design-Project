from draw_control import DrawControl

if __name__ == '__main__':
    zotter = DrawControl()

    test = input("track, rail, pen, hor, ver, diag: ")

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
            steps = input('steps: ')
            s = int(steps)
            zotter.draw_hor_line(0, s)

        elif test == "ver":
            steps = input('steps: ')
            s = int(steps)
            zotter.draw_ver_line(0, s)

        elif test == "diag":
            steps1 = input('x steps: ')
            steps2 = input('y steps: ')
            s1 = int(steps1)
            s2 = int(steps2)
            zotter.draw_diagonal(1, 1, s1, s2)

        test = input("track, rail, pen, hor, ver, diag: ")

    zotter.close_board()