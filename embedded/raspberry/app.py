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

import os
import json
import collections

import flask

from camera import Camera
from light_controller import LightController, LEDBoard

STOP_FLAG = True
LIGHTS_STATUS = {"red": None, "yellow": None, "green": None}

app = flask.Flask(__name__)
camera = Camera()


@app.route('/live', methods=['GET'])
def live():
    '''
    GET /live
    ---------
    Returns a stream from a .jpg generator using the Raspberry camera.
    '''

    return flask.Response(
        camera.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/status', methods=['GET'])
def status():
    '''
    GET /status
    -----------
    Returns the current status of the traffic light.
    '''

    return flask.jsonify(LIGHTS_STATUS)


@app.route('/animation', methods=['POST'])
def animation():
    '''
    POST /change_lights
    -------------------
    Stores a new submitted animation json file.
    '''
    data = flask.request.json

    def compare(list1, list2):
        return collections.Counter(list1) == collections.Counter(list2)

    if compare(['name', 'fps', 'looped', 'frames'], data.keys()):
        return "Invalid animation json.", 400

    with open('animations/{}.json'.format(data['name']), 'w') as animation_file:
        json.dump(data, animation_file)


@app.route('/change_lights', methods=['POST'])
def change_lights():
    '''
    POST /change_lights
    -------------------
    Sets the traffic lights to display certain passed animations.
    '''

    global STOP_FLAG
    STOP_FLAG = True
    STOP_FLAG = False

    available_animations = [x.split('.')[0] for x in os.listdir('animations/')]

    global LIGHTS_STATUS
    LIGHTS_STATUS['red'] = flask.request.args.get('red')
    LIGHTS_STATUS['yellow'] = flask.request.args.get('yellow')
    LIGHTS_STATUS['green'] = flask.request.args.get('green')

    if LIGHTS_STATUS['red'] in available_animations:
        with open('animations/{}.json'.format(LIGHTS_STATUS['red'])) as animation_file:
            animation = json.load(animation_file)
            LightController.display_animation(
                animation.frames, LEDBoard.RED, animation.fps, animation.looped, STOP_FLAG)
    else:
        return "Invalid animation passed for \"red\".", 400

    if LIGHTS_STATUS['yellow'] in available_animations:
        with open('animations/{}.json'.format(LIGHTS_STATUS['yellow'])) as animation_file:
            animation = json.load(animation_file)
            LightController.display_animation(
                animation.frames, LEDBoard.YELLOW, animation.fps, animation.looped, STOP_FLAG)
    else:
        return "Invalid animation passed for \"yellow\".", 400

    if LIGHTS_STATUS['green'] in available_animations:
        with open('animations/{}.json'.format(LIGHTS_STATUS['green'])) as animation_file:
            animation = json.load(animation_file)
            LightController.display_animation(
                animation.frames, LEDBoard.GREEN, animation.fps, animation.looped, STOP_FLAG)
    else:
        return "Invalid animation passed for \"green\".", 400

    return status()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
