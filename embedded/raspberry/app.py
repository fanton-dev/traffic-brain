import os
import json
import flask
from camera import Camera
from light_controller import LightController, LEDBoard

app = flask.Flask(__name__)
camera = Camera()


@app.route('/live', methods=['GET'])
def live():
    return flask.Response(camera.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/capture', methods=['GET'])
def capture():
    return flask.Response(camera.get_frame(), mimetype='image/jpeg')


@app.route('/status', methods=['GET'])
def status():
    pass


@app.route('/change_lights', methods=['GET'])
def change_lights():
    global stop_flag
    stop_flag = True
    stop_flag = False

    available_animations = [x.split('.')[0] for x in os.listdir('animations/')]
    args_passed = {
        'red':    flask.request.args.get('red'),
        'yellow': flask.request.args.get('yellow'),
        'green':  flask.request.args.get('green')}

    if args_passed['red'] in available_animations:
        with open('animations/{}.json'.format(args_passed['red'])) as animation_file:
            animation = json.load(animation_file)
            LightController.display_animation(
                animation.frames, LEDBoard.RED, animation.fps, animation.looped, stop_flag)
    else:
        return "Invalid animation passed for \"red\".", 400

    if args_passed['yellow'] in available_animations:
        with open('animations/{}.json'.format(args_passed['yellow'])) as animation_file:
            animation = json.load(animation_file)
            LightController.display_animation(
                animation.frames, LEDBoard.YELLOW, animation.fps, animation.looped, stop_flag)
    else:
        return "Invalid animation passed for \"yellow\".", 400

    if args_passed['green'] in available_animations:
        with open('animations/{}.json'.format(args_passed['green'])) as animation_file:
            animation = json.load(animation_file)
            LightController.display_animation(
                animation.frames, LEDBoard.GREEN, animation.fps, animation.looped, stop_flag)
    else:
        return "Invalid animation passed for \"green\".", 400

    return flask.jsonify(args_passed)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
