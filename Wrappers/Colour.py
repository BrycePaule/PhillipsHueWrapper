
class Colour:

    colour_maps = {
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'pink': (255, 0, 255),
        'purple': (127, 0, 255),
        'cyan': (0, 127, 255),
        'light_blue': (0, 255, 255),
        'yellow': (255, 255, 0),
        'orange': (255, 127, 0),
    }

    def __init__(self, colour):
        if type(colour) is str:
            self.rgb = self.colour_maps[colour.lower()]
            self.r = self.rgb[0]
            self.g = self.rgb[1]
            self.b = self.rgb[2]
        elif type(colour) is tuple:
            self.rgb = colour
            self.r = self.rgb[0]
            self.g = self.rgb[1]
            self.b = self.rgb[2]

    def as_xy(self):
        X = (0.4124 * self.r) + (0.3576 * self.g) + (0.1805 * self.b)
        Y = (0.2126 * self.r) + (0.7152 * self.g) + (0.0722 * self.b)
        Z = (0.0193 * self.r) + (0.1192 * self.g) + (0.9505 * self.b)

        if X + Y + Z == 0:
            return [0, 0]
        x = X / (X + Y + Z)
        y = Y / (X + Y + Z)

        return [x, y]

    def __repr__(self):
        return f'{self.__class__.__name__}{self.rgb}'
