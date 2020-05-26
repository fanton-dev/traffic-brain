'''
Blueprint of the '/information' server path.

This module contains a Flask server containing handlers for the following paths:
    - GET /live
        Returns a stream from a .jpg generator using the Raspberry camera.

    - GET /status
        Returns the current status of the traffic light.

Usage:
    from server.information.views import information_blueprint
    app.register_blueprint(information_blueprint)
'''

### Imports ###
from flask import Response, Blueprint, jsonify
from server.models.camera import Camera


### Config ###
information_blueprint = Blueprint('information', __name__)
LIGHTS_STATUS = {"red": None, "yellow": None, "green": None}


### Routes ###
@information_blueprint.route('/information/live', methods=['GET'])
def live():
    '''
    GET /live
    ---------
    Returns a stream from a .jpg generator using the Raspberry camera.
    '''

    camera = Camera()
    return Response(camera.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@information_blueprint.route('/information/status', methods=['GET'])
def status():
    '''
    GET /status
    -----------
    Returns the current status of the traffic light.
    '''

    return jsonify(LIGHTS_STATUS)
