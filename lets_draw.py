import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from parser import Parser

PRECISION = 2
SCALE = 30
STYLE = "default"
STYLE_RECEIVED = False
STYLE_PATH = ""
IMAGE_PATH = ""
parser = Parser()


def on_created(event):
    global STYLE_RECEIVED, PRECISION, SCALE, STYLE, STYLE_PATH, IMAGE_PATH
    print(f"{event.src_path} has been created!")

    file_path = f"{event.src_path}"
    time.sleep(2)

    if file_path.__contains__("style"):
        STYLE_PATH = file_path
        style_file = open(file_path, 'r')
        style = style_file.readlines()[0]

        if style.__contains__("default"):
            PRECISION = 2
            SCALE = 30
            STYLE = "default"
        elif style.__contains__("dotted"):
            PRECISION = 10
            SCALE = 30
            STYLE = "dotted"
        elif style.__contains__("abstract"):
            PRECISION = 15
            SCALE = 30
            STYLE = "abstract"
        STYLE_RECEIVED = True

        print("style set to: " + str(PRECISION) + " " + str(SCALE) + " " + STYLE)

    if file_path.__contains__("png") or file_path.__contains__("jpg") or file_path.__contains__("jpeg"):
        IMAGE_PATH = file_path
        if STYLE_RECEIVED:
            parser.parse_image(file_path, PRECISION, SCALE)
            if STYLE == "default":
                parser.run("instructions.txt")
            elif STYLE == "dotted":
                parser.run_dots("instructions.txt")
            elif STYLE == "abstract":
                parser.run_abstract("instructions.txt")

            STYLE_RECEIVED = False
            # os.remove(STYLE_PATH)
            # os.remove(IMAGE_PATH)

            print("style recieved: " + STYLE + "drawing")


if __name__ == "__main__":
    event_handler = PatternMatchingEventHandler("*", "", False, True)

    event_handler.on_created = on_created

    # path = "/home/pi/Downloads/"
    path = "/Users/eric/Desktop/test"
    my_observer = Observer()
    my_observer.schedule(event_handler, path, recursive=True)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()