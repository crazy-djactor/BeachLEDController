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