######!bin/bash

#add opencv-nonfree model
sudo add-apt-repository --yes ppa:xqms/opencv-nonfree
sudo apt-get update
sudo apt-get install build-essential -y
sudo apt-get install libboost-dev -y
sudo apt-get install make cmake -y
sudo apt-get install pkg-config -y
sudo apt-get install git -y
sudo apt-get install qt5-default qtcreator qt5-doc -y
#sudo apt-get install libcv2.4  -y
sudo apt-get install libopencv-dev -y
sudo apt-get install libopencv-nonfree-dev -y
#sudo apt-get install motion
sudo apt-get install nautilus-open-terminal -y
sudo apt-get install cmake-gui -y
sudo apt-get install tree -y
sudo apt-get install libfftw3-dev -y
#sudo apt-get install sabam

mkdir ~/git
#cd ~/git & git clone https://github.com/andrewssobral/bgslibrary.git

#sudo gedit /etc/profile
#export PKG_CONFIG_PATH=/usr/local/Qt5.5.1/5.5/gcc/lib/pkgconfig:$PKG_CONFIG_PATH
#export LD_LIBRARY_PATH=/usr/local/Qt5.5.1/5.5/gcc/lib:$LD_LIBRARY_PATH
#export CMAKE_MODULE_PATH=/usr/local/Qt5.5.1/5.5/gcc/lib/cmake:$CMAKE_MODULE_PATH
#export PATH=/usr/local/Qt5.5.1/5.5//gcc/bin:$PATH
