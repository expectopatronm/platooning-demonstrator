#!/bin/bash

echo "Installing necessary packages and libraries (don't quite know the difference though)."

sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install git
sudo pip3 install pyserial pillow numpy matplotlib

echo "Installing stuff that's required for pygame."

sudo apt-get install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev
sudo apt-get install libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev
sudo apt-get install libfreetype6-dev
sudo apt-get install libportmidi-dev
sudo pip3 install pygame

echo "Setting root permissions to the plugged in Arduino Uno on the USB UART."

sudo usermod -a -G dialout $USER

echo "Installing Tensorflow."

sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev
sudo pip3 install -U pip testresources setuptools
sudo pip3 install -U numpy==1.16.1 future==0.17.1 mock==3.0.5 h5py==2.9.0 keras_preprocessing==1.0.5 keras_applications==1.0.8 gast==0.2.2 enum34 futures protobuf

sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v43 tensorflow-gpu

echo "Installing PyTorch."

wget https://drive.google.com/file/d/1Eq641Jqb2Q0KBKsVpAhU-vxB_Mqcfrjd/view

sudo pip3 install torch-1.0.0a0+18eef1d-cp36-cp36m-linux_aarch64.whl
sudo pip3 install torchvision

sudo python3 -m pip install git+https://github.com/ipython/traitlets@master

echo "Installing Jupyter Lab."

sudo apt install nodejs npm
sudo pip3 install jupyter jupyterlab
sudo jupyter labextension install @jupyter-widgets/jupyterlab-manager
sudo jupyter labextension install @jupyterlab/statusbar
jupyter lab --generate-config

echo "You will be prompted to enter a password for the Jupyter Lab, maybe go for jetson/jetson2 (unless you want to use a custom password)."

jupyter notebook password

sudo pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension

echo "Cloning a Jetbot repo to use something inside the utils folder of it."

sudo apt install python3-smbus
git clone https://github.com/NVIDIA-AI-IOT/jetbot
cd jetbot
sudo apt-get install cmake
cd jetbot/utils
python3 create_jupyter_service.py
sudo mv jetbot_jupyter.service /etc/systemd/system/jetbot_jupyter.service
sudo systemctl enable jetbot_jupyter
sudo systemctl start jetbot_jupyter
cd ~

echo "Making a 6GB swapfile and mounting it on boot."

sudo fallocate -l 6G /var/swapfile
sudo chmod 600 /var/swapfile
sudo mkswap /var/swapfile
sudo swapon /var/swapfile
sudo bash -c 'echo "/var/swapfile swap swap defaults 0 0" >> /etc/fstab'

echo "Installing the PlayStation Dual Shock Controller Driver"

sudo pip3 install ds4drv

echo "Done!"