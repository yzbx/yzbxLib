# install opencv for centos!
yum -y update
yum list available opencv\*
yum groupinstall 'Development Tools'
yum install cmake git pkgconfig
yum install libpng-devel libjpeg-turbo-devel jasper-devel openexr-devel libtiff-devel libwebp-devel
yum install libdc1394-devel libv4l-devel gstreamer-plugins-base-devel
yum install gtk2-devel
yum install python-devel
pip install numpy
