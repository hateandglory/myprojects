
!nvidia-smi

import os
HOME = os.getcwd()
print(HOME)

!pip install ultralytics==8.0.20

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()

from ultralytics import YOLO

from IPython.display import display, Image

!mkdir {HOME}/datasets

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="OEYs5x2XzT9mvzgqTBXy")
project = rf.workspace("david-beliuzhenko-kbkbb").project("screw-detection-test")
dataset = project.version(21).download("yolov8")

!yolo task=detect mode=train model=yolov8l.pt data={dataset.location}/data.yaml epochs=110 imgsz=640 plots=True
