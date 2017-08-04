# install opencv for centos!
yum -y update
yum list available opencv\*
yum -y groupinstall 'Development Tools'
yum -y install cmake git pkgconfig
yum -y install libpng-devel libjpeg-turbo-devel jasper-devel openexr-devel libtiff-devel libwebp-devel
yum -y install libdc1394-devel libv4l-devel gstreamer-plugins-base-devel
yum -y install gtk2-devel
yum -y install python-devel
pip -y install numpy
