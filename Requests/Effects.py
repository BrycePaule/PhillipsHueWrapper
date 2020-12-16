import random
from time import sleep

from CustomObjects.Colour import Colour
from CustomObjects.Action import Action
from Requests.BasicCommands import send_actions
from CustomObjects.LightGroup import LightGroup
from Utilities.utils import increment_index, roll, offset_val_by_percentage
from itertools import cycle


def fade_between(lights: LightGroup, colours, fade_time=10, brightness=100, alternate_lights=False):
    if len(colours) < 2:
        return

    index = 0
    while True:
        for i, light in enumerate(lights):
            if alternate_lights:
                colour = colours[increment_index(index, len(colours), i + 1)]
            else:
                colour = colours[index]

            action = Action(light, on=True, colour=colour, transition_time=fade_time, bri=brightness)
            send_actions([action])

        sleep(fade_time)

        index = increment_index(index, len(colours))


def flash_between(lights, colours, flash_delay=0.3, brightness=100, alternate_lights=False):
    if len(colours) < 2:
        return

    index = 0
    while True:
        for i, light in enumerate(lights):
            if alternate_lights:
                colour = colours[increment_index(index, len(colours), i + 1)]
            else:
                colour = colours[index]

            action = Action(light, on=True, colour=colour, bri=brightness)
            send_actions([action])
        index = (index + 1) % len(colours)
        sleep(flash_delay)


def blink(lights, colours, flash_time, count=1):
    colours = [colours] if type(colours) == Colour else colours

    index = 0
    while count > 0:
        for light in lights:
            action = Action(light, on=True, colour=colours[index], bri=100, alert='select')
            send_actions([action])
        sleep(flash_time)

        index = (index + 1) % len(colours)
        if count != -1:
            count -= 1


def lava_lamp(lights, colour, transition_time=10, brightness=100, similarity_percent=20):
    while True:
        for light in lights:

            # chance to blink
            if roll(5):
                send_actions([Action(light, on=False, transition_time=transition_time)])
                continue

            offset_brightness = offset_val_by_percentage(brightness, similarity_percent, clamp_val=True, lower=0, upper=100)
            offset_colour = Colour.random_similar(colour, similarity_percent)

            action = Action(light, on=True, colour=offset_colour, bri=offset_brightness, transition_time=transition_time)
            send_actions([action])

        sleep(transition_time)
