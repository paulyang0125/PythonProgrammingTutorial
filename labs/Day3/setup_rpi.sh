

############################################
# setup_rpi.sh
# Author: Paul Yang
# Date: June, 2016
# Brief: set up raspberry-pi python Dev environment 
############################################

echo "##############################"
echo "1. apt update"
echo "##############################"
sleep 2
sudo apt-get update
sudo apt-get dist-upgrade


echo "##############################"
echo "2. install python3 DevEnvs"
echo "##############################"
sleep 2
sudo apt-get install -y ipython3-notebook python3-dev python3-pip geany geany-plugin-py bpython3  
sudo apt-get install -y samba samba-common-bin
sudo pip3 install virtualenv



echo "##############################"
echo "3. install HW i2c and spi modules"
echo "##############################"
sleep 2
sudo apt-get install -y python3-smbus python3-spidev rpi.gpio


echo "##############################"
echo "4. install dev tools"
echo "##############################"
sleep 2
sudo apt-get install -y vim ctags automake subversion gedit git tightvncserver
sudo apt-get install -y samba samba-common-bin


echo "##############################"
echo "5. pip install modules required in the class"
echo "##############################"
sleep 2
sudo apt-get install python3-flask python3-numpy python3-scipy python3-matplotlib python3-pandas python3-pandas-lib python3-lxml python3-requests 
sudo pip3 install sympy
sudo pip3 install beautifulsoup4sudo 
