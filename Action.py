from Colour import Colour
from utils import clamp, as_percentage


class Action:

    def __init__(
            self,
            light_id: int,
            on: bool = None,
            bri: int = None,
            hue: int = None,
            sat: int = None,
            colour: Colour = None,
            ct: int = None,
            effect: str = None,
            alert: str = None,
            transition_time: int = None
    ):
        self.light_id = light_id
        self.on = on
        self.bri = bri * (254 // 100) if bri else None
        self.hue = clamp(hue, 0, 65535) if hue else None
        self.sat = sat * (254 // 100) if sat else None
        self.xy = colour.as_xy() if colour else None
        self.ct = ct
        self.effect = effect
        self.alert = alert
        self.transitiontime = transition_time

    def as_dict(self):
        args = self.__dict__
        useful_keys = [key for key in args.keys() if args[key] is not None]
        return {k: args[k] for k in useful_keys if k != 'light_id'}
