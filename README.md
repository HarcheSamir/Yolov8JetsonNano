# YOLOv8-Based Real Time Weapon Detection System for Jetson Nano 



## Installation
• Get a 32 GB (minimal) SD card to hold the image.  
• Download the image [JetsonNanoUb20_3b.img.xz](https://ln5.sync.com/dl/403a73c60/bqppm39m-mh4qippt-u5mhyyfi-nnma8c4t/view/default/14418794280004) (8.7 GByte!).  
• Flash the image on the SD card with [balenaEtcher](https://etcher.balena.io/) after format.  
• Insert the SD card in your Jetson Nano .  
• Password: `jetson`



## Usage
```terminal
python3 -m pip install ultralytics.
git clone https://github.com/HarcheSamir/Yolov8JetsonNano.
cd Yolov8JetsonNano
python3 vidTest.py # or webCam.py to use with attached cameras
```   


