from track_control import TrackControl

"""
    Primary source for drawing control. Implements the usage of TrackControl and RailControl
    functions to draw an Image.

"""

TRACK_PIN_STEP = 0
TRACK_PIN_DIRECTION =0
TRACK_PIN_MS1 = 0
TRACK_PIN_MS2 = 0

RAIL_PIN_STEP = 0
RAIL_PIN_DIRECTION =0
RAIL_PIN_MS1 = 0
RAIL_PIN_MS2 = 0

class DrawControl:
    track = None
    rail = None

    def __init__(self):
        self.track = TrackControl(TRACK_PIN_STEP, TRACK_PIN_DIRECTION, TRACK_PIN_MS1, TRACK_PIN_MS2)
        self.rail = TrackControl(RAIL_PIN_STEP, RAIL_PIN_DIRECTION, RAIL_PIN_MS1, RAIL_PIN_MS2)



if __name__ == '__main__':
    zotter = DrawControl()
