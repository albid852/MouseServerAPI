import websockets
import asyncio
from functools import partial
from mouseController import MouseController


async def _get_scroll(websocket, path):
    async for scroll in websocket:
        print(scroll)


async def _get_command(websocket, path):
    async for command in websocket:
        print(command)


class MainServer:
    def __init__(self, target: MouseController, host: str, click_port, scroll_port, motion_port, command_port):
        self.target = target
        self.host = host
        self.click_port = click_port
        self.scroll_port = scroll_port
        self.motion_port = motion_port
        self.command_port = command_port

    async def _get_motion(self, websocket, path):
        async for accel in websocket:
            self.target.move(accel)

    async def _get_click(self, websocket, path):
        async for click in websocket:
            self.target.click(click)

    def run(self):
        async_runner = asyncio.get_event_loop().run_until_complete
        partial_get_motion = partial(self._get_motion)

        # can't use self in functions below for handlers, need a workaround....
        async_runner(websockets.serve(self._get_click, self.host, self.click_port))
        async_runner(websockets.serve(_get_scroll, self.host, self.scroll_port))
        async_runner(websockets.serve(partial_get_motion, self.host, self.motion_port))
        async_runner(websockets.serve(_get_command, self.host, self.command_port))

        asyncio.get_event_loop().run_forever()
