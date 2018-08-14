from app import create_app
from sanic_script import Manager
from runserver import RunServerCommand


app = create_app()
manager = Manager(app)


manager.add_command('server', RunServerCommand)

if __name__ == '__main__':
    manager.run()




