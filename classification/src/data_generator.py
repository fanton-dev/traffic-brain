import os
import xml.etree.ElementTree
import numpy as np
import tensorflow as tf


class DataGenerator():
    @staticmethod
    def parse_annotations(annotation_folder: str, image_dir: str, labels: list):
        '''
        Extracts bounding box information from PASCAL VOC .xml annotation files.

        Parameters:
        ----------
            annotation_folder : str
                Dataset annotations location.
            image_dir : str
                Dataset images location.
            labels : list
                Object labels to be parsed.

        Returns:
        --------
            A tuple containing:
                image_names : nparray
                    Images files paths (shape : image_count, 1)
                image_annotations : nparray
                    Annotations every image (shape : image count, max annotation count, 5) with
                    annotations in format xmin, ymin, xmax, ymax, class.
        '''
        max_annotations = 0
        image_names = []
        annotations = []

        for annotation in sorted(os.listdir(annotation_folder)):
            annotation_count = 0
            object_bboxes = []

            for element in xml.etree.ElementTree.parse(annotation_folder + annotation).iter():
                if 'filename' in element.tag:
                    image_names.append(image_dir + element.text)
                if 'width' in element.tag:
                    width = int(element.text)
                if 'height' in element.tag:
                    height = int(element.text)
                if 'object' in element.tag:
                    bbox = np.zeros((5))
                    annotation_count += 1
                    try:
                        bbox[4] = labels.index(element.find('name').text) + 1
                    except ValueError:
                        object_bboxes.append(np.asarray(bbox))
                        continue
                    for attr in list(element):
                        if 'bndbox' in attr.tag:
                            for dim in list(attr):
                                if 'xmin' in dim.tag:
                                    bbox[0] = int(
                                        round(float(dim.text))) / width
                                if 'ymin' in dim.tag:
                                    bbox[1] = int(
                                        round(float(dim.text))) / height
                                if 'xmax' in dim.tag:
                                    bbox[2] = int(
                                        round(float(dim.text))) / width
                                if 'ymax' in dim.tag:
                                    bbox[3] = int(
                                        round(float(dim.text))) / height
                    object_bboxes.append(np.asarray(bbox))
            annotations.append(np.asarray(object_bboxes))

            if annotation_count > max_annotations:
                max_annotations = annotation_count

        image_names = np.array(image_names)
        image_bboxes = np.zeros((image_names.shape[0], max_annotations, 5))
        for idx, bboxes in enumerate(annotations):
            image_bboxes[idx, :bboxes.shape[0], :5] = bboxes

        return image_names, image_bboxes
