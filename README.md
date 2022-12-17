# Raspberry Pi Keyboard emulator
Turning a Raspberry Pi into a keyboard emulator to automatically execute commands.
Additionally this Repo contains a translator script that translates the desired commands to be executed by the raspberry into a script.


Instructions based on:
- http://www.isticktoit.net/?p=1383
- https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/

Keyboard mapping achieved with the following information:
- [USB HID Usage table](https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf)

## Preparation
### 1. Enabling Modules and Drivers
    echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
    echo "dwc2" | sudo tee -a /etc/modules
    sudo echo "libcomposite" | sudo tee -a /etc/modules

### 2. Configuring the Gadget
1. Add the "usb_config" file to:  
`/usr/bin/`  
2. Make it executable:  
`sudo chmod +x /usr/bin/usb_config`  
3. The configuration is volatile, so it must run on each startup.  
Add the following line to the `/etc/rc.local` file, before he line containing *exit 0*  
`/usr/bin/usb_config`

### 3. Commands to be executed
1. Save your commands which the raspberry should execute in a *.txt* file.  
2. run the translator with the commands file as argument:  
`python translator.py commands.txt`  
This will generate the *cmd_to_strokes.py* file which will execute the keystrokes.  

### 4. Time to stroke
Connect your Raspberry to a Computer via USB and run the *cmd_to_strokes.py* script.  




**_NOTE:_** At the moment only swiss keyboard mapping is available
