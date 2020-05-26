'''
Module interface for controlling the embedded traffic lights connected
to the Raspberry Pi. The 3 16x16 LED matrices are controlled by 2 shift
registers each. This module presents the means for loading a sequence of
16x16 frames onto each of the boards.

Usage:
    The module could be used by importing it like shown:

        from light_controller import LightController, LEDBoard
'''

import time
from typing import List
from enum import Enum

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    class GPIO:
        '''
        Mock GPIO class for running the server on a non-Raspberry device.
        '''
        OUT = 'output'

        @staticmethod
        def setup(pin, mode):
            '''Mock GPIO setup'''
            print('[DEBUG] Setup pin {} to {}.'.format(pin, mode))

        @staticmethod
        def output(pin, state):
            '''Mock GPIO output'''
            print('[DEBUG] Output {} to pin {}.'.format(state, pin))

LOW = 0
HIGH = 1
ROW_SIZE = 16


class LEDBoard(Enum):
    '''
    Enum containing the colors of the 3 LED boards.

    Contains:
    ---------
        - RED
        - YELLOW
        - GREEN
    '''

    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'


class LightController():
    '''
    Class used for interacting with the embedded traffic lights.

    Parameters:
    -----------
    clock : int (default: 14)
        GPIO pin to be used clock synchronization.

    Red Light:
        data_bit_rx : int (default: 1)
            GPIO pin for pasing serial data to the rows controling shift register.
        data_bit_rxl : int (default: 2)
            GPIO pin for latch of the rows controling shift register.

        data_bit_ry : int (default: 3)
            GPIO pin for pasing serial data to the columns controling shift register.
        data_bit_ryl : int (default: 4)
            GPIO pin for latch of the columns controling shift register.

    Yellow Light:
        data_bit_rx : int (default: 5)
            GPIO pin for pasing serial data to the rows controling shift register.
        data_bit_rxl : int (default: 6)
            GPIO pin for latch of the rows controling shift register.

        data_bit_ry : int (default: 7)
            GPIO pin for pasing serial data to the columns controling shift register.
        data_bit_ryl : int (default: 8)
            GPIO pin for latch of the columns controling shift register.

    Green Light:
        data_bit_rx : int (default: 9)
            GPIO pin for pasing serial data to the rows controling shift register.
        data_bit_rxl : int (default: 10)
            GPIO pin for latch of the rows controling shift register.

        data_bit_ry : int (default: 11)
            GPIO pin for pasing serial data to the columns controling shift register.
        data_bit_ryl : int (default: 12)
            GPIO pin for latch of the columns controling shift register.
    '''

    def __init__(
            self,
            clock: int = 14,
            data_bit_rx: int = 1,
            data_bit_rxl: int = 2,
            data_bit_ry: int = 3,
            data_bit_ryl: int = 4,
            data_bit_yx: int = 5,
            data_bit_yxl: int = 6,
            data_bit_yy: int = 7,
            data_bit_yyl: int = 8,
            data_bit_gx: int = 9,
            data_bit_gxl: int = 10,
            data_bit_gy: int = 11,
            data_bit_gyl: int = 12,
    ):

        # Storing pin numbers (X - rows, Y - columns, L - latch)
        self.clock = clock
        self.data_bit_rx = data_bit_rx
        self.data_bit_rxl = data_bit_rxl
        self.data_bit_ry = data_bit_ry
        self.data_bit_ryl = data_bit_ryl
        self.data_bit_yx = data_bit_yx
        self.data_bit_yxl = data_bit_yxl
        self.data_bit_yy = data_bit_yy
        self.data_bit_yyl = data_bit_yyl
        self.data_bit_gx = data_bit_gx
        self.data_bit_gxl = data_bit_gxl
        self.data_bit_gy = data_bit_gy
        self.data_bit_gyl = data_bit_gyl

        # Setup IO
        GPIO.setup(self.clock, GPIO.OUT)
        GPIO.setup(self.data_bit_rx, GPIO.OUT)
        GPIO.setup(self.data_bit_rxl, GPIO.OUT)
        GPIO.setup(self.data_bit_ry, GPIO.OUT)
        GPIO.setup(self.data_bit_ryl, GPIO.OUT)
        GPIO.setup(self.data_bit_yx, GPIO.OUT)
        GPIO.setup(self.data_bit_yxl, GPIO.OUT)
        GPIO.setup(self.data_bit_yy, GPIO.OUT)
        GPIO.setup(self.data_bit_yyl, GPIO.OUT)
        GPIO.setup(self.data_bit_rx, GPIO.OUT)
        GPIO.setup(self.data_bit_rxl, GPIO.OUT)
        GPIO.setup(self.data_bit_ry, GPIO.OUT)
        GPIO.setup(self.data_bit_ryl, GPIO.OUT)

        GPIO.output(self.clock, LOW)
        GPIO.output(self.data_bit_rxl, LOW)
        GPIO.output(self.data_bit_ryl, LOW)
        GPIO.output(self.data_bit_yxl, LOW)
        GPIO.output(self.data_bit_yyl, LOW)
        GPIO.output(self.data_bit_gxl, LOW)
        GPIO.output(self.data_bit_gyl, LOW)

    def __pulsePin(self, pin: int):
        '''
        Pulse a given pin.

        Parameters:
        -----------
        pin : int
            GPIO pin a pulse to be send to.

        Returns:
        --------
        None.
        '''

        GPIO.output(pin, HIGH)
        GPIO.output(pin, LOW)

    def __ssrWrite(self, value: int, data_pin: int, latch_pin: int):
        '''
        Write a binary value through the serial input of the shift register.

        Parameters:
        -----------
        value : int
            The binary number to be written to the shift register.
        data_pin : int
            The shift register input data pin.
        data_pin : int
            The shift register input latch pin.

        Returns:
        --------
        None.
        '''

        for _ in range(0, ROW_SIZE):
            # If the MSB is 1 -> set the data_pin to HIGH, else set it to LOW
            # 0x8000 will take only the first bit of value and check if it's 1
            if value & 0x8000 == 0x8000:
                GPIO.output(data_pin, HIGH)
            else:
                GPIO.output(data_pin, LOW)

            # Pulse the Clock -> switch to next bit of serial input
            self.__pulsePin(self.clock)

            # Shift the value with 1 bit in order to get the next bit to push
            value = value << 0x0001

        # When it is all complete -> pulse the Latch so output is on parallel out
        self.__pulsePin(latch_pin)

    def display_frame(self, frame: List[List[int]], color: LEDBoard):
        '''
        Displays a given 2D frame on a given colored LED board.

        Parameters:
        -----------
        frame : List[List[int]]
            2D frame with ROW_SIZE x ROW_SIZE to be displayed on the LED frame.
        color : LEDBoard
            LEDBoard enum entry.

        Returns:
        --------
        None.
        '''

        # Defining bits to be serially pushed to the shift register
        x_bits = 0b1
        y_bits = 0b0

        for row in frame:
            # Switching the row (with color check)
            if color == 'red':
                self.__ssrWrite(x_bits, self.data_bit_rx, self.data_bit_rxl)
            if color == 'yellow':
                self.__ssrWrite(x_bits, self.data_bit_yx, self.data_bit_yxl)
            if color == 'green':
                self.__ssrWrite(x_bits, self.data_bit_gx, self.data_bit_gxl)

            # Convert row to bits. For ex:
            # [0, 1, 0, 0, 1] will turn into 9 or rather 0b01001
            for j, cell in enumerate(row):
                y_bits += cell * (2 ** j)

            # Displaying every cell of the row (with color check)
            if color == LEDBoard.RED:
                self.__ssrWrite(y_bits, self.data_bit_ry, self.data_bit_ryl)
            if color == LEDBoard.YELLOW:
                self.__ssrWrite(y_bits, self.data_bit_yy, self.data_bit_yyl)
            if color == LEDBoard.GREEN:
                self.__ssrWrite(y_bits, self.data_bit_gy, self.data_bit_gyl)

            # Shifting x for next row and reseting y
            x_bits = x_bits << 1
            y_bits = 0b0

    def display_animation(
            self,
            animation: List[List[List[int]]],
            color: LEDBoard,
            fps: float,
            looped: bool,
            multithread_stop_flag: bool = False
    ):
        '''
        Displays an animation on the LED board.

        Parameters:
        -----------
        frame : List[List[List[int]]]
            3D frame with FRAMES x ROW_SIZE x ROW_SIZE to be displayed on the LED frame.
        color : LEDBoard
            LEDBoard enum entry.
        fps : float
            Times the LED board refreshes in a second.
        looped : bool
            Whether or not to loop the whole animation.
        multithread_stop_flag : bool
            Used for multithreading, to stop a looped animation from the main thread.

        Returns:
        --------
        None.
        '''

        if fps <= 0:
            self.display_frame(animation[0], color)
            return

        for frame in animation:
            self.display_frame(frame, color)
            time.sleep(1 / fps)
            if multithread_stop_flag:
                return

        while looped:
            for frame in animation:
                self.display_frame(frame, color)
                time.sleep(1 / fps)
                if multithread_stop_flag:
                    return
