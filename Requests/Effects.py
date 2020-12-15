from time import sleep

from CustomObjects.Colour import Colour
from CustomObjects.Action import Action
from Requests.BasicCommands import send_actions
from CustomObjects.LightGroup import LightGroup


def fade_between(lights: LightGroup, colours, fade_time):
    if len(colours) < 2:
        return

    index = 0
    while True:
        for light in lights:
            action = Action(light.id, on=True, colour=colours[index], transition_time=fade_time)
            send_actions([action])

        index = (index + 1) % len(colours)


def flash_between(lights, colours):
    if len(colours) < 2:
        return

    index = 0
    while True:
        for light in lights:
            action = Action(light.id, on=True, colour=colours[index])
            send_actions([action])
        index = (index + 1) % len(colours)
        sleep(0.7)


def blink(lights, colours, flash_time, count=1):
    colours = [colours] if type(colours) == Colour else colours

    index = 0
    while count > 0:
        for light in lights:
            action = Action(light.id, on=True, colour=colours[index], bri=100, alert='select')
            send_actions([action])
        sleep(flash_time)

        index = (index + 1) % len(colours)
        if count != -1:
            count -= 1
