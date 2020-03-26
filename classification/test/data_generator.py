import os
import unittest
import configparser

import numpy as np

from src.data_generator import DataGenerator

with open('./config/classes.names') as class_file:
    LABELS = class_file.read().splitlines()

CONFIG = configparser.ConfigParser()
CONFIG.read('config/params.config')

IMAGE_W = int(CONFIG['YOLO']['IMAGE_W'])
IMAGE_H = int(CONFIG['YOLO']['IMAGE_H'])
GRID_W = int(CONFIG['YOLO']['GRID_W'])
GRID_H = int(CONFIG['YOLO']['GRID_H'])
BOXES = int(CONFIG['YOLO']['BOXES'])
CLASSES = int(CONFIG['YOLO']['CLASSES'])

IMAGE_FOLDER = os.path.dirname(os.path.realpath(__file__)) + '/images/'
ANNOTATION_FOLDER = os.path.dirname(
    os.path.realpath(__file__)) + '/annotations/'


class TestDataGenerator(unittest.TestCase):
    def test_parse_annotations(self):
        pass

    def test_generate_tf_dataset(self):
        pass

    def test_augment_dataset(self):
        pass

    def test_process_image_bboxes(self):
        pass


if __name__ == '__main__':
    unittest.main()
