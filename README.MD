## Light controller by Raspberry Pi

####Send request to backend to get light state of every beach
####Set 4 state light 
Device: https://wiki.52pi.com/index.php/DockerPi_4_Channel_Relay_SKU:_EP-0099
Module: https://github.com/geeekpi/dockerpi

####Run environment
sudo apt-get update
sudo apt-get -y install i2c-tools
sudo apt-get -y install git
pip3 install smbus2

####Config
SERVER_URL = "http://13.93.78.173:3000/ap1/v1/beaches/name/" 
BEACH_NAME = "Praia de Mogor"

#### Run
python3 main.py


##################################
https://www.waveshare.com/wiki/SIM868_PPP_Dail-up_Networking
