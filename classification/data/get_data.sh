#!/bin/sh
sha256sum -c checksum.txt --quiet
if [ $? -eq 1 ]
then
    rm VOCtrainval_11-May-2012.tar
    wget http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
fi

tar -xvf VOCtrainval_11-May-2012.tar
