# install necessary packages
sudo apt update -y && sudo apt upgrade -y
sudo apt install -y \
    python3-pyqt5 \
    python3-dev \
    wget

# download inputs
mkdir input
cd input/

# download pulp_fiction.mp4
FILEID="1Rv7PuahO3wlWqvnyS81zPpG0TcpE1u3U"
FILENAME="pulp_fiction.mp4"
FILEURL="https://docs.google.com/uc?export=download&id=$FILEID"
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate ${FILEURL} -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$FILEID" -O $FILENAME && rm -rf /tmp/cookies.txt

# download pulp_fiction_audio.mp3
FILEID="19LhfHev-QvszCwhQp-1TWjI90zpxGprM"
FILENAME="pulp_fiction.mp4"
FILEURL="https://docs.google.com/uc?export=download&id=$FILEID"
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate ${FILEURL} -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$FILEID" -O $FILENAME && rm -rf /tmp/cookies.txt

# ending download, back to previous folder
cd ..

# set virtualenv
python3 -m pip install virtualenv
python3 -m virtualenv env
source env/bin/activate

# install pip packages
pip3 install --upgrade pip
pip3 install -r requirements.txt
