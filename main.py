print("Hello, Pi Pico!")

from ClockController import *
from Displays import LCDDisplay
from Button import *
from Clock import *
from Counters import *

mydisplay = LCDDisplay(sda=0, scl=1, i2cid=0)

myclock = ClockController()


while True:
  myclock.showTime()
  time.sleep(1)