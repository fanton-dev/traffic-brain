#! /bin/bash
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
unzip ./VOCtrainval_11-May-2012.tar -d ./VOCtrainval

wget http://agamenon.tsc.uah.es/Personales/rlopez/data/rtm/Urban1.zip
unzip ./Urban1.zip -d ./Test1

wget http://agamenon.tsc.uah.es/Personales/rlopez/data/rtm/M-30.zip
unzip ./M-30.zip -d ./Test2