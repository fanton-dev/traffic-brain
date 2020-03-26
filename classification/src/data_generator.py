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

            # Goind through every markup element tag and storing whatever is required
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

                    # This try-except is used for checking if the object name is within classes
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

            # Max annotations exists so the image_bboxes shapes stay the same
            if annotation_count > max_annotations:
                max_annotations = annotation_count

        # Converting both lists to nparrays
        image_names = np.array(image_names)
        image_bboxes = np.zeros((image_names.shape[0], max_annotations, 5))

        # Reshaping image_bboxes
        for idx, bboxes in enumerate(annotations):
            image_bboxes[idx, :bboxes.shape[0], :5] = bboxes

        return image_names, image_bboxes

    @staticmethod
    def generate_tf_dataset(annotation_folder: str, image_dir: str, labels: list, batch_size: int):
        '''
        Creates a Tensorflow compatable dataset from YOLO images and annotations

        Parameters:
        -----------
            annotation_folder : str
                Dataset annotations location.
            image_dir : str
                Dataset images location.
            labels : list
                Object labels to be parsed.
            batch_size : int
                Image batch size.

        Returns:
        --------
            A batched Tensorflow dataset.
                batch : tuple
                    (images, annotations)
                        batch[0] : images : tensor (shape : batch_size, IMAGE_W, IMAGE_H, 3)
                        batch[1] : annotations : tensor (shape : batch_size, max annot, 5)
        '''
        # Parsing annotations
        image_names, image_bboxes = DataGenerator.parse_annotations(
            annotation_folder, image_dir, labels)

        # Creating a TF dataset from the parsed annotations nparrays
        tf_dataset = tf.data.Dataset.from_tensor_slices(
            (image_names, image_bboxes))

        # Shuffling the data
        tf_dataset = tf_dataset.shuffle(len(image_names))

        # Repeats dataset data indefinetly
        tf_dataset = tf_dataset.repeat()

        # Replaces every image filepath in the tf_dataset with a tensor containing all the pixel
        # values devided by 255, so they are floats between 0 and 1
        tf_dataset = tf_dataset.map(
            lambda image_object, image_bboxes: (
                tf.image.convert_image_dtype(
                    tf.image.decode_jpeg(
                        tf.io.read_file(image_object),
                        channels=3),
                    tf.float32),
                image_bboxes),
            num_parallel_calls=6)

        # Batching (grouping) togheter a given number images for training
        tf_dataset = tf_dataset.batch(batch_size)

        # From TF Dataset docs (https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch)
        # Most dataset input pipelines should end with a call to prefetch. This allows later
        # elements to be prepared while the current element is being processed. This often improves
        # latency and throughput, at the cost of using additional memory to store prefetched
        # elements.
        tf_dataset = tf_dataset.prefetch(10)

        return tf_dataset
