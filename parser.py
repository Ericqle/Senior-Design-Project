from draw_control import DrawControl
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv


class Parser:
    zotter_plotter = None
    HEIGHT_PAPER = 150
    WIDTH_PAPER = 250
    PRECISION = 50

    instructions = list()
    x_points = list()
    y_points = list()

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

    def run(self, filename):
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

    def run_dots(self, filename):
        instruction_file = open(filename, 'r')
        Instructions = instruction_file.readlines()

        for instruction in Instructions:
            instruction_elem = instruction.split(" ")
            x = int(instruction_elem[1])
            y = int(instruction_elem[2])
            self.execute_reposition(x, y)
            self.zotter_plotter.pen_down()
            self.zotter_plotter.pen_up()

    def parse_image(self, path):

        image = cv.imread(path)

        scale_x = self.WIDTH_PAPER / image.shape[1]
        scale_y = self.HEIGHT_PAPER / image.shape[0]

        imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(imgray, 127, 255, 0)

        # 2 GAUSSIAN
        blurredimg = cv.GaussianBlur(imgray, (3, 3), 0)  # odd only. greater = cleaner
        thresh = cv.adaptiveThreshold(blurredimg, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 3, 3)

        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(image, contours, 1, (0, 255, 0), 3)

        for contour in contours:
            reposition = False
            for point in contour[::self.PRECISION]:
                x = int(round(scale_x * point[0][0].item()))
                y = int(round(scale_y * point[0][1].item()))

                self.x_points.append(x)
                self.y_points.append(y)

                if not reposition:
                    instruction = "reposition " + str(x) + " " + str(y)
                    self.instructions.append(instruction)
                    reposition = True
                else:
                    instruction = "draw " + str(x) + " " + str(y)
                    self.instructions.append(instruction)

        file = open("instructions.txt", "w")
        for instruction in self.instructions:
            print(instruction)
            file.write(instruction + "\n")
        file.close()

        # plt.plot(self.x_points, self.y_points, 'ro')
        # plt.axis([0, 250, 0, 150])
        # plt.gca().invert_yaxis()
        # plt.gca().set_aspect('equal', adjustable='box')
        # plt.show()

        # cv.imshow('Contours', image)
        # cv.waitKey(0)
        # cv.destroyAllWindows()

if __name__ == '__main__':
    parser = Parser()
    parser.run("the_rock_instructions.txt")
    # parser.parse_image("images/peter.png")
    # parser.run_dots("instructions.txt")
    # parser.parse_image("images/abstract.jpg")
