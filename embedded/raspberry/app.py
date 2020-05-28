#!/usr/bin/env python
'''
Embedded traffic light Flask server.

This script will start a Flask server containing handlers for the following paths:
    - GET /live
        Returns a stream from a .jpg generator using the Raspberry camera.

    - GET /status
        Returns the current status of the traffic light.

    - POST /animation
        Stores a new submitted animation json file.

    - POST /change_lights
        Sets the traffic lights to display certain passed animations.

Usage:
    The server could be started by running::

        $ flask run
'''

from server import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
