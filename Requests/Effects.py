from time import sleep

from Wrappers.Colour import Colour
from Wrappers.Action import Action
from Requests.BasicCommands import send_actions


def fade_between(lights, colours, fade_time):
    if len(colours) < 2:
        return

    index = 0
    while True:
        for light in lights:
            action = Action(light, on=True, colour=colours[index], transition_time=fade_time)
            send_actions([action])
        index = (index + 1) % len(colours)


def bounce_between(lights, colours):
    if len(colours) < 2:
        return

    index = 0
    while True:
        for light in lights:
            action = Action(light, on=True, colour=colours[index])
            send_actions([action])
        index = (index + 1) % len(colours)
        sleep(0.3)


def flash(lights, colours, flash_time, count=-1):
    colours = [colours] if type(colours) == Colour else colours

    index = 0
    while count > 0:
        for light in lights:
            action = Action(light, on=True, colour=colours[index], bri=100, alert='select')
            send_actions([action])
            sleep(flash_time)

        index = (index + 1) % len(colours)



