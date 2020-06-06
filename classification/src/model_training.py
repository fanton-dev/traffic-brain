import ast
import configparser
import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as K

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
MIN_SCORE = float(CONFIG['YOLO']['MIN_SCORE'])
MIN_IOU = float(CONFIG['YOLO']['MIN_IOU'])
ANCHORS = ast.literal_eval(CONFIG['YOLO']['ANCHORS'])

TRAIN_BATCH_SIZE = int(CONFIG['TRAINING']['TRAIN_BATCH_SIZE'])
VAL_BATCH_SIZE = int(CONFIG['TRAINING']['VAL_BATCH_SIZE'])
EPOCHS = int(CONFIG['TRAINING']['EPOCHS'])

IMAGE_FOLDER = CONFIG['DIR']['IMAGES']
ANNOTATION_FOLDER = CONFIG['DIR']['ANNOTATIONS']


class ModelTraining:
    @staticmethod
    def loss(y_true, y_pred):
        '''
        YOLOv2 loss function.
        Sourced from https://github.com/guigzzz/Keras-Yolo-v2/blob/master/yolov2_train.py.

        Parameters:
        -----------
        y_true
        Returns:
        --------
        Calculated loss.
        '''

        y_true = tf.unstack(tf.reshape(
            y_true, [TRAIN_BATCH_SIZE * GRID_W * GRID_H * BOXES, 5 + CLASSES]))
        y_pred = tf.unstack(tf.reshape(
            y_pred, [TRAIN_BATCH_SIZE * GRID_W * GRID_H * BOXES, 5 + CLASSES]))

        # Confidence loss
        confidence_loss = 0
        for i, (true_grid_cell, pred_grid_cell) in enumerate(zip(y_true, y_pred)):
            confidence_loss += (true_grid_cell[4] - pred_grid_cell[4]) ** 2 + (
                true_grid_cell[4] - pred_grid_cell[4]) ** 2
            break

        loss = K.square(confidence_loss)
        print(loss)
        return loss

    @staticmethod
    def IOU(y_true, y_pred):
        print(y_pred, y_true)
        y_true = tf.unstack(tf.reshape(
            y_true, [TRAIN_BATCH_SIZE * GRID_W * GRID_H * BOXES, 5 + CLASSES]))
        y_pred = tf.unstack(tf.reshape(
            y_pred, [TRAIN_BATCH_SIZE * GRID_W * GRID_H * BOXES, 5 + CLASSES]))

        # Confidence loss
        iou = 0
        i = 0
        for i, (true_grid_cell, pred_grid_cell) in enumerate(zip(y_true, y_pred)):
            xmin1 = true_grid_cell[0] - 0.5*true_grid_cell[2]
            xmax1 = true_grid_cell[0] + 0.5*true_grid_cell[2]
            ymin1 = true_grid_cell[1] - 0.5*true_grid_cell[3]
            ymax1 = true_grid_cell[1] + 0.5*true_grid_cell[3]
            xmin2 = pred_grid_cell[0] - 0.5*pred_grid_cell[2]
            xmax2 = pred_grid_cell[0] + 0.5*pred_grid_cell[2]
            ymin2 = pred_grid_cell[1] - 0.5*pred_grid_cell[3]
            ymax2 = pred_grid_cell[1] + 0.5*pred_grid_cell[3]

            interx = tf.math.minimum(xmax1, xmax2) - tf.math.maximum(xmin1, xmin2)
            intery = tf.math.minimum(ymax1, ymax2) - tf.math.maximum(ymin1, ymin2)
            inter = interx * intery
            union = true_grid_cell[2]*true_grid_cell[3] + pred_grid_cell[2]*pred_grid_cell[3] - inter
            iou += inter / (union + 1e-6)
            break

        iou = iou / i
        iou = K.square(iou / i)
        return iou
