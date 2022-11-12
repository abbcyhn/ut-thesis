#!/bin/bash
set -e
echo "Installing OpenCV 4.5.0 on your Raspberry Pi 32-bit OS"
echo "It will take minimal 1.5 hour !"
cd ~
if [ -f /etc/os-release ]; then
    # freedesktop.org and systemd
    . /etc/os-release
    VER=$VERSION_ID
fi
# install the dependencies
apt-get install -y apt-utils build-essential cmake git unzip pkg-config
apt-get install -y libjpeg-dev libtiff-dev libpng-dev
apt-get install -y libavcodec-dev libavformat-dev libswscale-dev
apt-get install -y libgtk2.0-dev libcanberra-gtk* libgtk-3-dev
apt-get install -y libgstreamer1.0-dev gstreamer1.0-gtk3
apt-get install -y libgstreamer-plugins-base1.0-dev gstreamer1.0-gl
apt-get install -y libxvidcore-dev libx264-dev
if [ $VER == '11' ]; then
   echo "Detected Bullseye OS"
else
   apt-get install -y python-dev python-numpy python-pip
fi
apt-get install -y python3-dev python3-numpy python3-pip
apt-get install -y libtbb2 libtbb-dev libdc1394-22-dev
apt-get install -y libv4l-dev v4l-utils
apt-get install -y libopenblas-dev libatlas-base-dev libblas-dev
apt-get install -y liblapack-dev gfortran libhdf5-dev
apt-get install -y libprotobuf-dev libgoogle-glog-dev libgflags-dev
apt-get install -y protobuf-compiler
apt-get install -y wget

# remove old versions
cd ~ 
rm -rf opencv*
# download OpenCV
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.0.zip 
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.0.zip 
# unpack
unzip opencv.zip 
unzip opencv_contrib.zip 
# some administration to make live easier later on
mv opencv-4.5.0 opencv
mv opencv_contrib-4.5.0 opencv_contrib
# clean up the zip files
rm opencv.zip
rm opencv_contrib.zip

# set install dir
cd ~/opencv
mkdir build
cd build

# run cmake
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
-D ENABLE_NEON=ON \
-D ENABLE_VFPV3=ON \
-D WITH_OPENMP=ON \
-D BUILD_ZLIB=ON \
-D BUILD_TIFF=ON \
-D WITH_FFMPEG=ON \
-D WITH_TBB=ON \
-D BUILD_TBB=ON \
-D BUILD_TESTS=OFF \
-D WITH_EIGEN=OFF \
-D WITH_GSTREAMER=ON \
-D WITH_V4L=ON \
-D WITH_LIBV4L=ON \
-D WITH_VTK=OFF \
-D WITH_QT=OFF \
-D OPENCV_ENABLE_NONFREE=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D BUILD_opencv_python3=TRUE \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D PYTHON3_PACKAGES_PATH=/usr/lib/python3/dist-packages \
-D BUILD_EXAMPLES=OFF ..

# run make
make -j4
make install
ldconfig

# cleaning (frees 300 MB)
make clean
apt-get update

echo "Congratulations!"
echo "You've successfully installed OpenCV 4.5.0 on your Raspberry Pi 32-bit OS"