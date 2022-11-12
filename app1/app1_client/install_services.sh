sudo apt update && sudo apt upgrade
sudo apt install python
sudo apt install python-is-python3
sudo apt-get install python3-pip python3-virtualenv

python3 -m pip install virtualenv
python3 -m virtualenv env
source env/bin/activate

sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev

pip3 install --upgrade pip
pip3 install -r requirements.txt
