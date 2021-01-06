from flask import Flask
import asyncio


class Server(Flask):
    def __init__(self):
        super().__init__(__name__)
        self.async_loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.async_loop)

    def __del__(self):
        self.async_loop.stop()
