from sanic_script import Command, Option
from app import create_app
import os


class RunServerCommand(Command):
    """
    Run the HTTP/HTTPS server.
    """
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
