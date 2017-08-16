# install opencv for centos!
yum -y update
yum -y epel-release
yum list available opencv\*
yum -y groupinstall 'Development Tools'
yum -y install cmake git pkgconfig wget
#yum -y install libpng-devel libjpeg-turbo-devel jasper-devel openexr-devel libtiff-devel libwebp-devel
#yum -y install libdc1394-devel libv4l-devel gstreamer-plugins-base-devel
#yum -y install gtk2-devel
#yum -y install python-devel
#yum -y install python-pip
#yum -y install zsh autojump
wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
bash Miniconda2-latest-Linux-x86_64.sh -b
echo "$HOME/miniconda2/bin" >> ~/.bashrc
source ~/.bashrc
pip -y install numpy opencv_python opencv_contrib_python django
