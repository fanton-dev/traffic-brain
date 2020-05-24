import cv2


class CameraReadFailedException(Exception):
    pass


class Camera:
    def __init__(self, camera=cv2.VideoCapture(0)):
        self.camera = camera

    def generate_frames(self):
        while True:
            try:
                frame = Camera.get_frame(self)
            except CameraReadFailedException:
                continue

            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'

    def get_frame(self):
        success, frame = self.camera.read()
        if not success:
            raise CameraReadFailedException

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        return frame
