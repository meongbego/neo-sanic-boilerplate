# NEO-SANIC PROJECT

This Boiler Plate From Sanic APP


## Environment File

``` bash
APP_NAME = app-name
APP_HOST = 127.0.0.1
APP_PORT = 5000
APP_VERSION = 0.0.0
APP_RELEASE = AAA
APP_CREATED = AAA
APP_WORKERS = 2
APP_DEBUG = True
APP_SSL = None

```

## Local Development

At the time neo-api only support Python3 or newer.

``` bash
pip3 install -r requirements.txt
```

After Installing Requirement File, Next Install redis


Use our locally default configuration
``` bash
cp env.example .env
```


Runing Server
``` bash
python manage.py server
```

## Testing

Go To Browser Open this Url: http://127.0.0.1:5000/api/test/people

