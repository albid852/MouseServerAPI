import websockets
import asyncio
import pyautogui


async def _get_click(websocket, path):
    async for click in websocket:
        print(click)
        code = int(click)
        if code == 0:
            print("left click")
            pyautogui.leftClick()
        if code == 1:
            print("right click")
            pyautogui.rightClick()
        if code == 2:
            print("middle click")
            pyautogui.middleClick()


async def _get_scroll(websocket, path):
    async for scroll in websocket:
        print(scroll)


async def _get_motion(websocket, path):
    async for motion in websocket:
        print(motion)


async def _get_command(websocket, path):
    async for command in websocket:
        print(command)


class MainServer:
    def __init__(self, host: str, click_port, scroll_port, motion_port, command_port):
        self.host = host
        self.click_port = click_port
        self.scroll_port = scroll_port
        self.motion_port = motion_port
        self.command_port = command_port

    def run(self):
        async_runner = asyncio.get_event_loop().run_until_complete

        async_runner(websockets.serve(_get_click, self.host, self.click_port))
        async_runner(websockets.serve(_get_scroll, self.host, self.scroll_port))
        async_runner(websockets.serve(_get_motion, self.host, self.motion_port))
        async_runner(websockets.serve(_get_command, self.host, self.command_port))

        asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    print("Starting server")
    HOST = "localhost"
    click_port = 5793
    scroll_port = 5794
    motion_port = 5795
    command_port = 5796

    main_server = MainServer(HOST, click_port, scroll_port, motion_port, command_port)
    main_server.run()
