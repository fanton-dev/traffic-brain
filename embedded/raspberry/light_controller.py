#!/usr/bin/env python
import time
from typing import List
from enum import Enum

import RPi.GPIO as GPIO

LOW = 0
HIGH = 1
ROW_SIZE = 16


class LEDBoard(Enum):
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'


class LightController():
    def __init__(
            self,
            clock: int = 14,
            data_bit_rx: int = 1,
            data_bit_ry: int = 2,
            data_bit_rl: int = 3,
            data_bit_yx: int = 4,
            data_bit_yy: int = 5,
            data_bit_yl: int = 6,
            data_bit_gx: int = 7,
            data_bit_gy: int = 8,
            data_bit_gl: int = 9
    ):

        # Storing pin numbers (X - rows, Y - columns, L - latch)
        self.clock = clock
        self.data_bit_rx = data_bit_rx
        self.data_bit_ry = data_bit_ry
        self.data_bit_rl = data_bit_rl
        self.data_bit_yx = data_bit_yx
        self.data_bit_yy = data_bit_yy
        self.data_bit_yl = data_bit_yl
        self.data_bit_gx = data_bit_gx
        self.data_bit_gy = data_bit_gy
        self.data_bit_gl = data_bit_gl

        # Setup IO
        GPIO.setup(self.clock, GPIO.OUT)
        GPIO.setup(self.data_bit_rx, GPIO.OUT)
        GPIO.setup(self.data_bit_ry, GPIO.OUT)
        GPIO.setup(self.data_bit_rl, GPIO.OUT)
        GPIO.setup(self.data_bit_yx, GPIO.OUT)
        GPIO.setup(self.data_bit_yy, GPIO.OUT)
        GPIO.setup(self.data_bit_yl, GPIO.OUT)
        GPIO.setup(self.data_bit_gx, GPIO.OUT)
        GPIO.setup(self.data_bit_gy, GPIO.OUT)
        GPIO.setup(self.data_bit_gl, GPIO.OUT)

        GPIO.output(self.data_bit_rl, LOW)
        GPIO.output(self.data_bit_yl, LOW)
        GPIO.output(self.data_bit_gl, LOW)
        GPIO.output(self.clock, LOW)

    def _pulsePin(self, pin: int):
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

    def _ssrWrite(self, value: int, data_pin: int, latch_pin: int):
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
            self._pulsePin(self.clock)

            # Shift the value with 1 bit in order to get the next bit to push
            value = value << 0x0001

        # When it is all complete -> pulse the Latch so output is on parallel out
        self._pulsePin(latch_pin)

    def display_frame(self, frame: List[int, int], color: LEDBoard):
        '''
        Displays a given 2D frame on a given colored LED board.

        Parameters:
        -----------
        frame : List[int, int]
            2D frame with ROW_SIZE x ROW_SIZE to be displayed on the LED frame.
        color : LEDBoard
            LEDBoard enum entry.

        Returns:
        --------
        None.
        '''

        # Defining bits to be serially pushed to the shift register
        x = 0b1
        y = 0b0

        for row in frame:
            # Switching the row (with color check)
            if color == 'red':
                self._ssrWrite(x, self.data_bit_rx, self.data_bit_rl)
            if color == 'yellow':
                self._ssrWrite(x, self.data_bit_yx, self.data_bit_yl)
            if color == 'green':
                self._ssrWrite(x, self.data_bit_gx, self.data_bit_gl)

            # Convert row to bits. For ex:
            # [0, 1, 0, 0, 1] will turn into 9 or rather 0b01001
            for j, cell in enumerate(row):
                y += cell * (2 ** j)

            # Displaying every cell of the row (with color check)
            if color == LEDBoard.RED:
                self._ssrWrite(y, self.data_bit_ry, self.data_bit_rl)
            if color == LEDBoard.YELLOW:
                self._ssrWrite(y, self.data_bit_yy, self.data_bit_yl)
            if color == LEDBoard.GREEN:
                self._ssrWrite(y, self.data_bit_gy, self.data_bit_gl)

            # Shifting x for next row and reseting y
            x = x << 1
            y = 0b0

    def display_animation(
            self,
            animation: List[int, int, int],
            color: LEDBoard,
            fps: float,
            looped: bool,
            multithread_stop_flag: bool = False
    ):
        '''
        Displays an animation on the LED board.

        Parameters:
        -----------
        frame : List[int, int, int]
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
