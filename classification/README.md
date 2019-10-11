# YOLO (You Only Look Once) Implementation for Traffic Assesment
YOLO (You only look once) is a widely used in computer vision tasks such as face detection, object recognition and etc.

## Training the classification model
First, we need to setup the working enviourment. An easy way to get started is to install docker and the tensorflow image. This could be done by doing the following.

#### Installing Docker
Instructions on installing Docker could be found [in this manual](https://docs.docker.com/install/linux/docker-ce/ubuntu/).

#### Installing a Docker Tensorflow image
For **CPU-only** supporting image run the following:
``` 
$ docker run -it -v $(pwd):/tf -p 8888:8888 tensorflow/tensorflow:nightly-gpu-py3-jupyter
```

Or alternatively, for a **GPU** supporting image run the following:
```
$ docker run -it --runtime=nvidia -v $(pwd):/tf -p 8888:8888 tensorflow/tensorflow:nightly-gpu-py3-jupyter
```
*Note: To train the model on a GPU, you first need to setup **nvidia-docker**. Instruction refrence could be found [here](https://www.tensorflow.org/install/docker#gpu_support).*

#### Opening the notebook
The notebook should be accessible on ```localhost:8888``` with the access token printed in the command-prompt.