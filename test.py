from draw_control import DrawControl

if __name__ == '__main__':
    zotter = DrawControl()

    test = input("track, rail, pen, hor, ver, diag: ")

    while(test):
        if test == "track":
            dir_in = input('0 cw 1  ccw: ')
            dir = dir_in.split(" ")
            zotter.track.spin_fixed_step(int(dir[0]), int(dir[1]))

        elif test == "rail":
            dir_in = input('0 cw 1  ccw: ')
            dir = dir_in.split(" ")
            zotter.rail.spin_fixed_step(int(dir[0]), int(dir[1]))

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
            dir_in = input('dir1 dir2 steps1 steps2: ')
            dir = dir_in.split(" ")
            zotter.draw_diagonal(int(dir[0]), int(dir[1]), int(dir[2]), int(dir[3]))

        test = input("track, rail, pen, hor, ver, diag: ")

    zotter.close_board()