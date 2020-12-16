from CustomObjects.Colour import Colour
from Utilities.utils import clamp
from CustomObjects.Light import Light


class Action:

    """
    light: Light
    on : bool
    bri : int [0, ..., 100]
    hue : int [0, ..., 65535]
    sat : int [0, ..., 100]
    colour : Colour
    ct : int [0, ..., 500]
    effects : [colorloop]
    alert : [select, lselect]
    transition_time : int in centiseconds (10 = 1s)
    """

    def __init__(
            self,
            light: Light,
            on: bool = None,
            bri: int = None,
            hue: int = None,
            sat: int = None,
            colour: Colour = None,
            ct: int = None,
            effect: str = None,
            alert: str = None,
            transition_time: int = None,

            xy: list = None,
    ):
        self.light = light
        self.on = on
        self.bri = int((bri / 100) * 254) if bri else None
        self.hue = clamp(hue, 0, 65535) if hue else None
        self.sat = int((sat / 100) * 254) if sat else None
        self.xy = colour.as_xy() if colour else None
        self.ct = ct
        self.effect = effect
        self.alert = alert
        self.transitiontime = transition_time * 10 if transition_time else 0

        if xy:
            self.xy = xy

    def as_dict(self):
        args = self.__dict__
        useful_keys = [key for key in args.keys() if args[key] is not None]
        return {k: args[k] for k in useful_keys if k != 'light'}
