'''
Interface for taking data from the connected to the Raspberry Pi camera.

Usage:
    The module could be used by importing it like shown:

        from camera import Camera
'''
import cv2


class CameraReadFailedException(Exception):
    '''
    CameraReadFailedException: If camera read (camera got disconnected, camera is used by
    another application) fails exception is thrown.
    '''


class Camera:
    '''
    Interface for taking data from the connected to the Raspberry Pi camera.

    Parameters:
    -----------
    camera : VideoCapture
        CV2 camera device to capture from.
    '''

    def __init__(self, camera=cv2.VideoCapture(0)):
        self.camera = camera

    def __del__(self):
        self.camera.release()

    def generate_frames(self):
        '''
        Captures a livestreams from the CV2 camera and returns it.

        Parameters:
        -----------
        None.

        Returns:
        -------
        A generator of JPG frames.
        '''

        while True:
            try:
                frame = Camera.get_frame(self)
            except CameraReadFailedException:
                continue

            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'

    def get_frame(self):
        '''
        Captures a frame from the CV2 camera.

        Parameters:
        -----------
        None.

        Returns:
        -------
        JPG frame bytes.

        Raises:
        -------
        CameraReadFailedException: If camera read (camera got disconnected, camera is used by
        another application) fails exception is thrown.
        '''

        success, frame = self.camera.read()
        if not success:
            raise CameraReadFailedException

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        return frame
