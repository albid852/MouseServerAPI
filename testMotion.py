from mouseController import MouseController

dt = 1.0 / 60.0
mc = MouseController(dt)

accel = "['x': 0.62211, 'y': -0.62211]"

for i in range(350):
    mc.move(accel)
