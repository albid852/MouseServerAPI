import pyautogui
import time


def decode_vector(vec: str) -> dict:
    vec_list = vec[1:-1].split(", ")  # remove [ ] and split at ,
    keys = list(map(lambda s: s[: s.index(":")].strip("'").strip("\""), vec_list))
    values = list(map(lambda s: float(s[s.index(":") + 1:].strip(" ")), vec_list))
    return dict(zip(keys, values))


def calculate_dr(a, dt, v):
    # vf = {'x': a['x'] * dt + v['x'], 'y': a['y'] * dt + v['x']}
    dr = {'dx': a['x'] * dt * dt, 'dy': a['y'] * dt * dt}

    # dr = {'dx': vf['x'] * dt, 'dy': vf['y'] * dt}
    # v['x'] = vf['x']
    # v['y'] = vf['y']
    return dr


class MouseController:

    def __init__(self, dt):
        self.dt = dt
        self.v = {'x': 0, 'y': 0}
        self.lastClicked = time.perf_counter()

    def update_last_clicked(self):
        self.lastClicked = time.perf_counter()

    def click(self, click):
        print(click)
        code = click[0]
        action = click[1]
        if code == "0":
            if action == "0":
                print("left click")
                pyautogui.leftClick()
            elif action == "1":
                if self.lastClicked - time.perf_counter() < 1:
                    print("double click")
                    pyautogui.doubleClick(button='left')
                else:
                    print("left down")
                    pyautogui.mouseDown(button='left')
                self.update_last_clicked()

            elif action == "2":
                print("left up")
                pyautogui.mouseUp(button='left')
        elif code == "1":
            if action == "0":
                print("right click")
                pyautogui.rightClick()
            elif action == "1":
                print("right down")
                pyautogui.mouseDown(button='right')
            elif action == "2":
                print("right up")
                pyautogui.mouseUp(button='right')
        elif code == "2":
            if action == "0":
                print("middle click")
                pyautogui.middleClick()
            elif action == "1":
                print("middle down")
                pyautogui.mouseDown(button='middle')
            elif action == "2":
                print("middle up")
                pyautogui.mouseUp(button='middle')

    def move(self, accel):
        a = decode_vector(accel)
        if abs(a['x']) < 0.05 and abs(a['y']) < 0.05:
            return
        # print(accel)
        dr = calculate_dr(a, self.dt, self.v)
        # print(round(dr['dx'] * 10 ** 5), round(dr['dy'] * 10 ** 5))
        # FIND BETTER SCALING FACTOR THAN 100!
        # It moves, but there's too much noise and positional drift
        # find way to better calculate this...
        pyautogui.moveRel(round(dr['dx'] * 10 ** 6), round(dr['dy'] * 10 ** 6), duration=self.dt)

