# Object detection based on the YOLOv2 architecture
> YOLOv2 (You only look once) is a widely used in computer vision tasks such as face detection, object recognition, etc. This is a Tensorflow 2.1.0 implementation of the same architecture (with slight modifications) for traffic assesment. 

<p align="center">
<a href="https://github.com/braind3d/traffic-brain/actions?query=workflow%3A%22Classification+CI">
<img src="https://img.shields.io/github/workflow/status/braind3d/traffic-brain/Classification+CI?style=flat-square" alt="Classification CI status">
</a>

<a href="https://github.com/braind3d/traffic-brain/issues?q=is%3Aopen+is%3Aissue+label%3Aclassification">
<img src="https://img.shields.io/github/issues-raw/braind3d/traffic-brain/classification?label=open%20issues&style=flat-square" alt="Classification open issues badge">
</a>

<a href="https://github.com/braind3d/traffic-brain/issues?q=is%3Aissue+label%3Aclassification+is%3Aclosed">
<img src="https://img.shields.io/github/issues-closed-raw/braind3d/traffic-brain/classification?label=closed%20issues&style=flat-square" alt="Classification closed issues badge">
</a>

<a href="LICENSE">
<img src="https://img.shields.io/github/license/braind3d/traffic-brain?style=flat-square" alt="License badge">
</a>
</p>

## Getting started
<!-- ### Test the deployed model
If you only want to test the predictions  -->
### Run in Google Collab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/braind3d/traffic-brain/blob/master/classification/YOLO_Traffic_classification.ipynb)

The Jupyter notebook could be viewed in Google Collab via the link [here](https://colab.research.google.com/github/braind3d/traffic-brain/blob/master/classification/YOLO_Traffic_classification.ipynb).

### Run locally
First, we need to setup the working enviourment for the project. A simple way of doing so is  Another relateivly easy way to get started is to install [`Docker`](https://docs.docker.com/install/linux/docker-ce/ubuntu/) and the official `Tensorflow` image.

### Setup with Docker

#### Installing a Docker Tensorflow 
Which image you should install primairly depends on whether you have NVIDIA Cuda drivers installed. If so, you will need to install [`nvidia-docker`](https://www.tensorflow.org/install/docker#gpu_support) and you will be able to run the GPU supported [`tensorflow/tensorflow:nightly-gpu-py3-jupyter`](https://hub.docker.com/r/tensorflow/tensorflow/tags?page=1&name=nightly-gpu-py3-jupyter) image. Otherwise you can still run the CPU-only image - [`tensorflow/tensorflow:nightly-py3-jupyter`](https://hub.docker.com/r/tensorflow/tensorflow/tags?page=1&name=nightly-py3-jupyter).

For `CPU-only` supporting image run the following:
``` 
$ docker run -it -v $(pwd):/tf -p 8888:8888 tensorflow/tensorflow:nightly-py3-jupyter
```

For `GPU` supporting image run the following:
```
$ docker run -it --runtime=nvidia -v $(pwd):/tf -p 8888:8888 tensorflow/tensorflow:nightly-gpu-py3-jupyter
```

#### Opening the notebook
The notebook should be accessible on `localhost:8888` with the access token printed in the command-prompt.

## How does it work?
You can a much more detailed explanation on YOLOv1 in the research paper - [here](paper/yolov1.pdf) and on YOLOv2 - [here](paper/yolov2.pdf).

## Built With
**Python 3.7** with the following libraries:
- Tensorflow (2.1.0) - Neural network model
- Numpy (1.18.2) - Data formating
- Pillow - Loading images
- Jupyter Notebook (1.0.0) - IDE
- MatPlotLib (3.2.1) - Data visualization

## License
Distributed under the MIT license. See [LICENSE](../LICENSE) for more information.