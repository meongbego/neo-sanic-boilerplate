from sanic_script import Command, Option
from app import create_app
from signal import signal, SIGINT
import os
import asyncio
import uvloop


class RunServerCommand(Command):
    app = create_app()

    option_list = (
        Option('--host', '-h', dest='host'),
        Option('--port', '-p', dest='port'),
    )

    def run(self, *args, **kwargs):
        self.app.run(
            host=os.getenv('APP_HOST'),
            port=int(os.getenv('APP_PORT')),
            debug=os.getenv('APP_DEBUG'),
            ssl=None,
            workers=int(os.getenv('APP_WORKERS'))
        )
        asyncio.set_event_loop(uvloop.new_event_loop())
        server = self.app.create_server(
            host=os.getenv('APP_HOST'),
            port=int(os.getenv('APP_PORT')),
            debug=os.getenv('APP_DEBUG')
        )
        signal(SIGINT, lambda s, f: loop.stop())
        loop = asyncio.get_event_loop()
        task = asyncio.ensure_future(server)
        try:
            loop.run_forever()
        except:
            loop.stop()