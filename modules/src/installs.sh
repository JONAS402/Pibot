#!/bin/bash

echo "                       *************
                       **JONAS_402**
                       ************* 
"
echo "setting up mysql Database for Dejavu"
mysql -u root < "./create_dejavu_database.sql"

if [ -e ./Opencv ]
then
    echo "Open cv is already installed"
else
    echo "checking everything is up-to-date..."
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y dist-upgrade
sudo apt-get -y autoremove

# INSTALL THE DEPENDENCIES
# Build tools:
echo "Installing... Build Tools"
sudo apt-get install -y build-essential cmake
# GUI:
echo "Installing... GUI"
sudo apt-get install -y qt5-default libvtk6-dev
# Media I/O:
echo "Installing... Media I/O"
sudo apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libjasper-dev libopenexr-dev libgdal-dev
# Video I/O:
echo "Installing... Video I/O"
sudo apt-get install -y libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev
# Parallelism and linear algebra libraries:
echo "Installing... Parallelism and linear algebra libraries"
sudo apt-get install -y libtbb-dev libeigen3-dev
# Python:
echo "Installing... Python Extras"
sudo apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk python3-numpy
# Java:
echo "Installing... Java"
sudo apt-get install -y ant default-jdk
# Documentation:
echo "Installing... Documentation"
sudo apt-get install -y doxygen
# INSTALL THE LIBRARY (YOU CAN CHANGE '3.0.0' FOR THE LAST STABLE VERSION)
sudo apt-get install -y unzip wget
echo "Installing... Wget"
echo "downloading... Open-CV 3.0.0.zip"
wget https://github.com/Itseez/opencv/archive/3.0.0.zip
echo "unzipping and cleaning..."
unzip 3.0.0.zip
rm 3.0.0.zip
mv opencv-3.0.0 OpenCV
cd OpenCV
mkdir build
cd build
echo "Making Open-CV 3.0.0"
cmake -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON -DWITH_GDAL=ON -DWITH_XINE=ON -DBUILD_EXAMPLES=ON ..
make -j4
echo "Installing Open-CV 3.0.0"
sudo make install
echo "Running... ldconfig"
sudo ldconfig
echo "Installation Complete"
fi
