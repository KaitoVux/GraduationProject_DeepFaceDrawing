echo -e '\033[41;37m If you cannot download the pre-trained models automatically, please download them yourself and put them under the 'Params' fold \033[0m'

# Create a virtual environment 
virtualenv --no-site-packages -p python3.7 ~/DeepFaceDrawing

# Activate the virtual environment
source ~/DeepFaceDrawing/bin/activate

# Update pip
python3.7 -m pip install -U pip

# install necessary libraries
python3.7 -m pip install jittor==1.2.2.09
python3.7 -m pip install pyqt5==5.9.2
python3.7 -m pip install Pillow==8.0.1
python3.7 -m pip install scipy==1.5.4
python3.7 -m pip install dominate==2.6.0
python3.7 -m pip install opencv-python==4.1.0.25
mv ./heat/bg.jpg ./heat/.jpg

# download pretrained model
rm -rf Params
mkdir Params
cd ./Params
wget -O Combine.zip https://www.dropbox.com/s/5s5c4zuq6jy0cgc/Combine.zip
unzip Combine.zip && rm Combine.zip
wget -O AE_whole.zip https://www.dropbox.com/s/cs4895ci51h8xn3/AE_whole.zip
unzip AE_whole.zip && rm AE_whole.zip

# run code
cd ..
python3.7 demo.py
