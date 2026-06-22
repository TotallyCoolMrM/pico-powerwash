import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(.5)


import time

#trigger powerwash
kbd.press(
    Keycode.CONTROL,
    Keycode.ALT,
    Keycode.SHIFT,
    Keycode.R
)
kbd.release_all()


time.sleep(5)


kbd.press(Keycode.TAB)
kbd.release_all()
time.sleep(.1)
kbd.press(Keycode.TAB)
kbd.release_all()
time.sleep(.1)
kbd.press(Keycode.TAB)
kbd.release_all()
time.sleep(.1)
kbd.press(Keycode.TAB)
kbd.release_all()
time.sleep(.1)
kbd.press(Keycode.TAB)
kbd.release_all()
time.sleep(.1)



  
kbd.press(Keycode.ENTER)
kbd.release_all()                                          

time.sleep(5)

kbd.press(Keycode.TAB)
kbd.release_all()
time.sleep(.1)
kbd.press(Keycode.ENTER)
kbd.release_all()
time.sleep(.1)

while True:
    pass