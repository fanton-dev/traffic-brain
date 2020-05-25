'''
Blueprint of the '/traffic-light' server path.

This module contains a Flask server containing handlers for the following paths:
    - POST /traffic-light/animation
        Stores a new submitted animation json file.

    - POST /traffic-light/change_lights
        Sets the traffic lights to display certain passed animations.

Usage:
    from server.traffic_light.views import traffic_light_blueprint
    app.register_blueprint(traffic_light_blueprint)
'''

### Imports ###
import os
import json
import collections
from flask import request, Blueprint

from server.models.light_controller import LightController, LEDBoard
from server.information.views import status
from server.information.views import LIGHTS_STATUS


### Config ###
traffic_light_blueprint = Blueprint('traffic-light', __name__)
light_controller = LightController()
STOP_FLAG = True


### Helpers ###
def load_animation(name: str, color: LEDBoard):
    '''
    Loads an animation from a given name

    Parameters:
    -----------
    name : str
        Name of the animations to be loaded.

    color : LEDBoard
        The board on which the animation should be displayed.
    '''
    with open('../static/animations/{}.json'.format(name)) as animation_file:
        animation = json.load(animation_file)
        light_controller.display_animation(
            animation.frames, color, animation.fps, animation.looped, STOP_FLAG)


### Routes ###
@traffic_light_blueprint.route('/traffic-light/animation', methods=['POST'])
def animation():
    '''
    POST /change_lights
    -------------------
    Stores a new submitted animation json file.
    '''
    data = request.json

    def compare(list1, list2):
        return collections.Counter(list1) == collections.Counter(list2)

    if compare(['name', 'fps', 'looped', 'frames'], data.keys()):
        return "Invalid animation json.", 400

    with open('../static/animations/{}.json'.format(data['name']), 'w') as animation_file:
        json.dump(data, animation_file)

    return "OK", 200


@traffic_light_blueprint.route('/traffic-light/change_lights', methods=['POST'])
def change_lights():
    '''
    POST /change_lights
    -------------------
    Sets the traffic lights to display certain passed animations.
    '''

    global STOP_FLAG
    STOP_FLAG = True
    STOP_FLAG = False

    available_animations = [x.split('.')[0]
                            for x in os.listdir('static/animations/')]

    global LIGHTS_STATUS
    LIGHTS_STATUS['red'] = request.args.get('red')
    LIGHTS_STATUS['yellow'] = request.args.get('yellow')
    LIGHTS_STATUS['green'] = request.args.get('green')

    if LIGHTS_STATUS['red'] in available_animations:
        load_animation(LIGHTS_STATUS['red'], LEDBoard.RED)
    else:
        return "Invalid animation passed for \"red\".", 400

    if LIGHTS_STATUS['yellow'] in available_animations:
        load_animation(LIGHTS_STATUS['yellow'], LEDBoard.RED)
    else:
        return "Invalid animation passed for \"yellow\".", 400

    if LIGHTS_STATUS['green'] in available_animations:
        load_animation(LIGHTS_STATUS['green'], LEDBoard.GREEN)
    else:
        return "Invalid animation passed for \"green\".", 400

    return status()
