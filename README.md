# Share the Unseen

## Dependencies

This repository assumes an Ubuntu distribution (it was developed and tested on Ubuntu 20.04.1 LTS). 
In this readme file we will explain how to install all required dependencies for this tutorial, which are:
1. Anaconda :snake:
2. Jupyter notebook :notebook_with_decorative_cover:
3. CommonRoad framework :oncoming_automobile: :oncoming_taxi: :oncoming_police_car:
4. SUMO (Simulation of Urban MObility)

## Step-by-step installation

1. Install Anaconda (https://docs.anaconda.com/anaconda/install/linux/)

2. Create a new conda environment and activate it.
```
$ conda create -n shared_occlusions python=3.8
$ conda activate shared_occlusions
```
3. Clone this repository and install its dependencies
```
$ cd /your/path
$ git clone https://gits-15.sys.kth.se/jmgs/share_the_unseen
$ cd share_the_unseen
$ pip install -r requirements.txt
$ sudo apt install ffmpeg
```
