import flask
import json
from camera import Camera

app = flask.Flask(__name__)


@app.route('/camera')
def video_feed():
    return flask.Response(Camera().gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/status', methods=['GET'])
def status():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0')
