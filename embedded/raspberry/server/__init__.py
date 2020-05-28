'''
Embedded traffic light Flask server.

This module contains a Flask server containing handlers for the following paths:
    - GET /information/live
        Returns a stream from a .jpg generator using the Raspberry camera.

    - GET /information/status
        Returns the current status of the traffic light.

    - POST /traffic-light/animation
        Stores a new submitted animation json file.

    - POST /traffic-light/change_lights
        Sets the traffic lights to display certain passed animations.

Module tree:
    .
    ├── information
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-36.pyc
    │   │   └── views.cpython-36.pyc
    │   └── views.py
    ├── __init__.py
    ├── models
    │   ├── camera.py
    │   ├── __init__.py
    │   ├── light_controller.py
    │   └── __pycache__
    │       ├── camera.cpython-36.pyc
    │       ├── __init__.cpython-36.pyc
    │       └── light_controller.cpython-36.pyc
    ├── __pycache__
    │   └── __init__.cpython-36.pyc
    ├── static
    │   └── animations
    │       ├── 3sec.json
    │       ├── empty.json
    │       └── filled.json
    ├── templates
    └── traffic_light
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-36.pyc
        │   └── views.cpython-36.pyc
        └── views.py

Usage:
    from server import create_app
    app = create_app()
    app.run(host='0.0.0.0', debug=True)

'''

from flask import Flask

from server.traffic_light.views import traffic_light_blueprint
from server.information.views import information_blueprint


def create_app(
        name: str = __name__,
        config: str = 'flask.cfg',
        blueprints: tuple = (traffic_light_blueprint, information_blueprint)
):
    '''
    Initializes the Flask server.

    Parameters:
    -----------
    name : str (default: __name__)
        Name of the server.

    config : str (default: 'flask.cfg')
        Configuration to be loaded.

    blueprints : tuple (default: traffic_light_blueprint, information_blueprint)
        Blueprint functions to be registered.

    Returns:
    --------
    A Flask server app.
    '''

    app = Flask(
        name,
        template_folder='templates',
        instance_relative_config=True
    )

    app.config.from_pyfile(config)

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
