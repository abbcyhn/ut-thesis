# download input video from google drive
# https://drive.google.com/file/d/1uX_g9OQJE6L0ZD_1HO8hNPeZyqcARLzJ/view?usp=share_link

FILEID = "1uX_g9OQJE6L0ZD_1HO8hNPeZyqcARLzJ"
FILENAME = "traffic.mp4"
FILEURL = "https://docs.google.com/uc?export=download&id=$FILEID"

wget --load-cookies /tmp/cookies.txt 
    / "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate ${FILEURL} -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$FILEID" 
    / -O $FILENAME && rm -rf /tmp/cookies.txt

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
