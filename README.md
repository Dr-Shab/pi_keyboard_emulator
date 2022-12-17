# Raspberry Pi Keyboard emulator
Turning a Raspberry Pi into a keyboard emulator to automatically execute commands.
Addiotionally this Repo contains a translator script that translates the desired commands to be executed by the raspberry into a script.


Instructions based on:
- http://www.isticktoit.net/?p=1383
- https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/

Keyboard mapping achieved with the following information:
- [USB HID Usage table](https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf)

## Preparation
### 1. Enabling Modules and Drivers
    `pi@raspberrypi:~ $ echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
    pi@raspberrypi:~ $ echo "dwc2" | sudo tee -a /etc/modules
    pi@raspberrypi:~ $ sudo echo "libcomposite" | sudo tee -a /etc/modules`
