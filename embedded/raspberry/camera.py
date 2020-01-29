import cv2

class Camera:
    def __init__(self, camera=cv2.VideoCapture(0)):
        self.camera = camera

    def gen_frames(self):
        while True:
            success, frame = self.camera.read()
            if not success:
                break

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
