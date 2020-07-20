## Light controller by Raspberry Pi

###Device configration
####Set external wifi dongle to use wifi
- sudo wget http://downloads.fars-robotics.net/wifi-drivers/install-wifi -O /usr/bin/install-wifi
- sudo chmod +x /usr/bin/install-wifi
- sudo install-wifi 

After installing driver using vnc you can easily setup your wifi.
####Headless wifi setup
- Create wpa_supplicant.conf in boot directory when install new system on raspberry pi.
  Put the following contents.
  
    country=US
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    network={
        ssid="NETWORK-NAME"
        psk="NETWORK-PASSWORD"
    }

- Set up after installation.
    Create wpa_supplicant.conf file with above contents in /etc/wpa_supplicant/ 
    
####Set PPP for SIM7000e-nb-iot HAT
Refer this https://www.waveshare.com/wiki/SIM868_PPP_Dail-up_Networking

- sudo apt-get install ppp
- sudo su
- cd /etc/ppp/peers
- cp provider gprs
- sudo nano gprs
  
  user "myusername@realm"
  connect "/user/sbin/chat -v -f /etc/chatscripts/gprs"
  /dev/ttyUSB2              //sim7000 - dev/ttyUSB2 or dev/ttyS0
  115200
  
  no crtscts
  debug
  nodetach
  ipcp-accpet-local
  ipcp-accept-remote
  
  noipdefault
  usepeerdns
  defaultroute
  persist
  noauth

- And edit /etc/chatscripts/gprs
 Here replace pin number and APN provider.
- Excute the command as below to run it in the background
  pppd call gprs &
  route add -net 0.0.0.0 ppp0
   
####Enable VNC and I2C of Raspberry pi
- Enable i2c and vnc configuration on raspi-config. VNC is easy way to control raspberry.
  
  
###Send request to backend to get light state of every beach
####Set  4 state light reference 
Device: https://wiki.52pi.com/index.php/DockerPi_4_Channel_Relay_SKU:_EP-0099
Module: https://github.com/geeekpi/dockerpi

####Run environment
sudo apt-get update
sudo apt-get -y install i2c-tools
sudo apt-get -y install git
pip3 install smbus2
"

#### Run
git clone https://github.com/crazy-djactor/BeachLEDController.git
 
cd BeachLeadController

pip3 install -r requirement.txt

python3 main.py

######Install services for running 24/7
cp ./controller.service /etc/systemd/system/led_controller.service
sudo systemctl daemon-reload
sudo systemctl start led_controller.service