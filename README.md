![Python](https://img.shields.io/badge/python-3.7-blue?style=flat-square)
![vJoy](https://img.shields.io/badge/vJoy-v2.1.9.1-blue?style=flat-square)
![Xbox360CE](https://img.shields.io/badge/Xbox%20360%20Controller%20Emulator-v4.17.15.0-blue?style=flat-square)

Idealogy
========

This program was made mainly for the use of cloud streaming. As of right now, there are many cloud streaming services on the market that only allow controller input. This program allows your keyboard and mouse to be used as a gamepad. 

Dependencies 
============

* `python` and `pip` then run `pip install -r requirements.txt`
* [vJoy](https://sourceforge.net/projects/vjoystick/)
* [Xbox 360 Controller Emulator](https://www.x360ce.com/)

Setup vJoy
==========

1. Open the Configure vJoy application
2. Select Device 1
3. Change the settings to look like so:

![vJoyConfiguration](/images/vJoyConfiguration.PNG)

Setup Controller Emulator
=========================

After setting up the Xbox 360 Controller Emulator, do the following:
1. Click on the controller 1 tab
2. Click on the "Add..." button 
3. Select the vJoy input device, hit "Add selected device" 
4. Add the following binds:

![Xbox 360 CE Configuration](/images/Xbox360CEConfiguration.PNG)