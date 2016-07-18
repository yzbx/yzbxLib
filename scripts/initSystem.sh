######!bin/bash

#add opencv-nonfree model
#sudo add-apt-repository --yes ppa:xqms/opencv-nonfree
sudo add-apt-repository --yes ppa:webupd8team/atom
sudo add-apt-repository --yes ppa:george-edison55/cmake-3.x
sudo add-apt-repository --yes ppa:lyx-devel/release
#sudo add-apt-repository ppa:mc3man/trusty-media
#python ide
#sudo apt-add-repository ppa:ninja-ide-developers/ninja-ide-stable
sudo apt-get update
sudo apt-get install atom
#sudo apt-get install ninja-ide
sudo apt-get install build-essential -y
sudo apt-get install libboost-dev -y
sudo apt-get install make cmake autoconf -y
sudo apt-get install pkg-config -y
sudo apt-get install git -y
#sudo apt-get install qt5-default qtcreator qt5-doc -y
#sudo apt-get install libopencv-dev -y
#sudo apt-get install libopencv-nonfree-dev -y
#sudo apt-get install motion
sudo apt-get install nautilus-open-terminal libgnome2-bin-y
sudo apt-get install cmake-gui -y
sudo apt-get install tree -y
sudo apt-get install synaptic -y
sudo apt-get install wget octave -y
sudo apt-get install lyx -y

#sudo apt-get install libfftw3-dev -y
#sudo apt-get install python-dev
# add ffmpeg support for opencv to use VideoCapture.
sudo apt-get install x264 v4l-utils ffmpeg -y
sudo apt-get install libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

# add for opencv + qt + ubuntu16.04 + python, remove gl.h error
sudo apt-get install libgl1-mesa-dev libglu1-mesa-dev

sudo apt-get install zeal

### add for cv2 model in python, but may not necessary
#sudo apt-get install python-opencv
mkdir ~/git
mkdir ~/config
mkdir ~/test
#cd ~/git & git clone https://github.com/andrewssobral/bgslibrary.git

#sudo gedit /etc/profile
export QT5_ROOT=/home/yzbx/linux/Qt5.6.0/5.6/gcc_64
export PKG_CONFIG_PATH=${QT5_ROOT}/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=${QT5_ROOT}/lib:${QT5_ROOT}/plugins/platforms:$LD_LIBRARY_PATH
export LIBRARY_PATH=${QT5_ROOT}/lib:${QT5_ROOT}/plugins/platforms:$LIBRARY_PATH
export CMAKE_MODULE_PATH=${QT5_ROOT}/lib/cmake:$CMAKE_MODULE_PATH
export PATH=${QT5_ROOT}/bin:$PATH
export PYTHONPATH=/usr/local/lib/python2.7/site-packages:${QT5_ROOT}/plugins/platforms:${QT5_ROOT}/lib:$PYTHONEPATH
export QT_QPA_PLATFORM_PLUGIN_PATH=${QT5_ROOT}/plugins

###gedit ~/.bashrc
# if [[ $- == *i* ]]
# then
#     bind '"\e[A": history-search-backward'
#     bind '"\e[B": history-search-forward'
# fi
