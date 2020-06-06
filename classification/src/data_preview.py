import matplotlib


class DataPreview():
    @staticmethod
    def preview_dataset(dataset):
        '''
        Displays dataset sample in a Jupyter notebook.

        Parameters:
        -----------
        dataset : tf.Dataset
        A batched Tensorflow dataset.
        batch : tuple
            (images, annotations)
                batch[0] : images : tensor (shape : batch_size, IMAGE_W, IMAGE_H, 3)
                batch[1] : annotations : tensor (shape : batch_size, max annot, 5)

        Returns:
        --------
        None.
        '''
        for batch in dataset:
            img = batch[0][0]
            label = batch[1][0]

            matplotlib.pyplot.figure()
            _, (ax1) = matplotlib.pyplot.subplots(1, 1, figsize=(10, 10))
            ax1.imshow(img)
            ax1.set_title('Input image. Shape : {}'.format(img.shape))
            for i in range(label.shape[0]):
                box = label[i, :]
                box = box.numpy()
                coord_x = box[0]
                coord_y = box[1]
                width = box[2] - box[0]
                height = box[3] - box[1]
                if box[4] == 1:
                    color = (0, 1, 0)
                else:
                    color = (1, 0, 0)
                rect = matplotlib.patches.Rectangle(
                    (coord_x, coord_y),
                    width,
                    height,
                    linewidth=2,
                    edgecolor=color,
                    facecolor='none')
                ax1.add_patch(rect)
            break
