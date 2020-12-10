from draw_control import DrawControl

class Parser:
    zotter_plotter = None

    def __init__(self):
        self.zotter_plotter = DrawControl()
        self.PEN_DOWN = 0
        self.CURRENT_X = 0
        self.CURRENT_Y = 0

    def execute_draw(self, x, y):
        num_steps1 = x - self.CURRENT_X
        num_steps2 = y - self.CURRENT_Y
        dir1 = 1
        dir2 = 1

        if num_steps1 < 0:
            dir1 = 0
        if num_steps2 < 0:
            dir2 = 0

        num_steps1 = abs(num_steps1)
        num_steps2 = abs(num_steps2)

        if self.PEN_DOWN == 0:
            self.zotter_plotter.pen_down()
            print("pen down")
            self.PEN_DOWN = 1

        if num_steps1 == 0:
            self.zotter_plotter.draw_ver_line(dir2, num_steps2)
            print("draw " + str(dir2) + " " + str(num_steps2))
        elif num_steps2 == 0:
            self.zotter_plotter.draw_hor_line(dir1, num_steps1)
            print("draw " + str(dir1) + " " + str(num_steps1))
        else:
            self.zotter_plotter.draw_diagonal(dir1, dir2, num_steps1, num_steps2)
            print("draw " + str(dir1) + " " + str(dir2) + " " + str(num_steps1) + " " + str(num_steps2))

        self.CURRENT_X = x
        self.CURRENT_Y = y

    def execute_reposition(self, x, y):
        num_steps1 = x - self.CURRENT_X
        num_steps2 = y - self.CURRENT_Y
        dir1 = 1
        dir2 = 1

        if num_steps1 < 0:
            dir1 = 0
        if num_steps2 < 0:
            dir2 = 0

        num_steps1 = abs(num_steps1)
        num_steps2 = abs(num_steps2)

        if self.PEN_DOWN == 1:
            self.zotter_plotter.pen_up()
            print("pen up")
            self.PEN_DOWN = 0

        if num_steps1 == 0:
            self.zotter_plotter.draw_ver_line(dir2, num_steps2)
            print("reposition " + str(dir2) + " " + str(num_steps2))
        elif num_steps2 == 0:
            self.zotter_plotter.draw_hor_line(dir1, num_steps1)
            print("reposition " + str(dir1) + " " + str(num_steps1))
        else:
            self.zotter_plotter.draw_diagonal(dir1, dir2, num_steps1, num_steps2)
            print("reposition " + str(dir1) + " " + str(dir2) + " " + str(num_steps1) + " " + str(num_steps2))

        self.CURRENT_X = x
        self.CURRENT_Y = y

    def parse_and_run(self, filename):
        instruction_file = open(filename, 'r')
        Instructions = instruction_file.readlines()

        for instruction in Instructions:
            instruction_elem = instruction.split(" ")

            if instruction_elem[0].__contains__("draw"):
                x = int(instruction_elem[1])
                y = int(instruction_elem[2])
                self.execute_draw(x, y)

            elif instruction_elem[0].__contains__("reposition"):
                x = int(instruction_elem[1])
                y = int(instruction_elem[2])
                self.execute_reposition(x, y)


if __name__ == '__main__':
    parser = Parser()
    parser.parse_and_run("instructions_peter.txt")

