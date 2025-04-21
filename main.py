from World import *

w = World()
w.start()

while 1:
    if w.play() == 0:
        break
