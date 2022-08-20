import microbit
from microbit import *

def on_gesture_screen_up():
    basic.show_icon(IconNames.GHOST)
    basic.clear_screen()
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

# beats taken from: https://makecode.microbit.org/44800-51100-77366-66449
def play_magalovania():
    basic.show_icon(IconNames.YES)
    basic.clear_screen()
    basic.show_icon(IconNames.ASLEEP)
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(587, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    basic.show_number(input.temperature())
    basic.clear_screen()
    if input.light_level() == 128:
        basic.show_number(input.light_level())
        basic.clear_screen()
        basic.show_icon(IconNames.SAD)
        basic.clear_screen()

def on_button_pressed_a():
    play_magalovania()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_icon(IconNames.SKULL)
    basic.clear_screen()
    basic.show_leds("""
        . # # # .
                # . # . #
                # # # # #
                . # . # .
                . # # # .
    """)
    basic.clear_screen()
basic.forever(on_forever)
