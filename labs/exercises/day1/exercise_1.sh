#!/bin/bash
############################################
# exercise_1.sh
# Author: Paul Yang
# Date: June, 2016
# Brief: installation procedures by conda
############################################

#Install by conda 
conda search beautifulsoup4 #Search for beautifulsoup4 package
conda install --name ittraining_py3 beautifulsoup4 #Install a new package
source activate ittraining_py3
conda list

#remove package by conda
conda remove --name ittraining_py3 beautifulsoup4

#Install from Anaconda.org (optional)
conda install --channel https://conda.anaconda.org/pandas bottleneck 
conda list
#Install by pip (optional)
source activate ittraining_py3
pip install beautifulsoup4
conda list

