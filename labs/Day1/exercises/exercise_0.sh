#!/bin/bash

############################################
# exercise_0.sh
# Author: Paul Yang
# Date: June, 2016
# Brief: set up Anaconda
############################################


echo "##############################"
echo "1. set up Anaconda"
echo "##############################"

bash Anaconda3-4.0.0-Linux-x86_64.sh
export PATH="/home/username/anaconda/bin:$PATH"
conda update conda 
conda update anaconda
conda create --name ittraining_py3 python=3
source activate ittraining_py3
conda info --envs
python –version 








