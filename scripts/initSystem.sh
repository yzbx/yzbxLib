######!bin/bash

#add opencv-nonfree model
sudo add-apt-repository --yes ppa:xqms/opencv-nonfree
sudo add-apt-repository --yes ppa:webupd8team/atom  
sudo add-apt-repository --yes ppa:george-edison55/cmake-3.x
sudo add-apt-repository ppa:mc3man/trusty-media
#python ide
sudo apt-add-repository ppa:ninja-ide-developers/ninja-ide-stable
sudo apt-get update
#sudo apt-get install atom 
#sudo apt-get install ninja-ide
sudo apt-get install build-essential -y
sudo apt-get install libboost-dev -y
sudo apt-get install make cmake autoconf -y
sudo apt-get install pkg-config -y
sudo apt-get install git -y
sudo apt-get install qt5-default qtcreator qt5-doc -y
sudo apt-get install libopencv-dev -y
sudo apt-get install libopencv-nonfree-dev -y
#sudo apt-get install motion
sudo apt-get install nautilus-open-terminal -y
sudo apt-get install cmake-gui -y
sudo apt-get install tree -y
sudo apt-get install libfftw3-dev -y
sudo apt-get install python-dev
sudo apt-get install ffmpeg

mkdir ~/git
#cd ~/git & git clone https://github.com/andrewssobral/bgslibrary.git

#sudo gedit /etc/profile
export QT5_ROOT=/home/yzbx/ComputerVision/Qt5.6.0/5.6/gcc_64
export PKG_CONFIG_PATH=${QT5_ROOT}/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=${QT5_ROOT}/lib:$LD_LIBRARY_PATH
export CMAKE_MODULE_PATH=${QT5_ROOT}/lib/cmake:$CMAKE_MODULE_PATH
export PATH=${QT5_ROOT}/bin:$PATH

#gedit ~/.bashrc
# ~/.bashrc
# if [[ $- == *i* ]]
# then
#     bind '"\e[A": history-search-backward'
#     bind '"\e[B": history-search-forward'
# fi
