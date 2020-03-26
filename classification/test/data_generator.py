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
        '''
        Unittest suite for DataGenerator.parse_annotations().

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        '''
        parsed_annotations = DataGenerator.parse_annotations(
            ANNOTATION_FOLDER,
            IMAGE_FOLDER,
            LABELS)

        # Validating the first array shape (1D, containing image filepaths (3))
        self.assertEqual(parsed_annotations[0].shape, (3,))

        # Validating the second array shape (3D, containing xmin, ymin, xmax, ymax, label (5) for
        # each annotation (max: 6) for each image (3))
        self.assertEqual(parsed_annotations[1].shape, (3, 6, 5))

        # Validating the first array data
        self.assertEqual(
            parsed_annotations[0].tolist(),
            [IMAGE_FOLDER + '{}.jpg'.format(i + 1) for i in range(3)])

        # Validating the second array data
        expected_result = [[[2.00e-03, 2.66666667e-03, 9.16e-01, 1.00000000e+00, 3],
                            [0.00e+00, 0.00000000e+00, 0.00e+00, 0.00000000e+00, 0],
                            [0.00e+00, 0.00000000e+00, 0.00e+00, 0.00000000e+00, 0],
                            [0.00e+00, 0.00000000e+00, 0.00e+00, 0.00000000e+00, 0],
                            [0.00e+00, 0.00000000e+00, 0.00e+00, 0.00000000e+00, 0],
                            [0.00e+00, 0.00000000e+00, 0.00e+00, 0.00000000e+00, 0], ],
                           [[0.00e+00, 0.00000000e+00, 0.00e+00, 0.00000000e+00, 0],
                            [0.00e+00, 0.00000000e+00, 0.00e+00, 0.00000000e+00, 0],
                            [0.00e+00, 0.00000000e+00, 0.00e+00, 0.00000000e+00, 0],
                            [0.00e+00, 0.00000000e+00, 0.00e+00, 0.00000000e+00, 0],
                            [0.00e+00, 0.00000000e+00, 0.00e+00, 0.00000000e+00, 0],
                            [0.00e+00, 0.00000000e+00, 0.00e+00, 0.00000000e+00, 0], ],
                           [[3.20e-01, 4.86486486e-01, 3.80e-01, 6.54654655e-01, 6],
                            [6.02e-01, 4.89489489e-01, 6.78e-01, 6.66666667e-01, 6],
                            [7.20e-02, 4.65465465e-01, 1.46e-01, 6.57657658e-01, 6],
                            [1.52e-01, 4.68468468e-01, 2.08e-01, 6.78678679e-01, 6],
                            [5.76e-01, 4.83483483e-01, 6.28e-01, 6.12612613e-01, 6],
                            [4.84e-01, 4.32432432e-01, 5.48e-01, 7.14714715e-01, 6]]]

        self.assertEqual(
            [[[[round(z)] for z in y] for y in x]
             for x in parsed_annotations[1].tolist()],
            [[[[round(z)] for z in y] for y in x] for x in expected_result])

    def test_generate_tf_dataset(self):
        pass

    def test_augment_dataset(self):
        pass

    def test_process_image_bboxes(self):
        pass


if __name__ == '__main__':
    unittest.main()
