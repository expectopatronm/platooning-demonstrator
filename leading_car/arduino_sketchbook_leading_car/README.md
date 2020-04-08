# remocar.core
Core components for controlling a RC Car using a Raspberry Pi

## T2 Workshop
* Connect to the RemoCar Raspberry Pi: `ssh pi@<raspi IP>`
* Start the data collection: `cd remocar.core; python3 motor_control_arduino.py`
* Drive the car using your smartphone by visiting `http://<raspi IP>:5000` in its browser, making sure both are in the same wifi network
* Data collection will stop once 500 images have been recorded. Stop the python script at any time with `Ctrl+C`.
* Compress the collected data: `./upload_training_data.sh`
* Follow the instructions detailed in the [T2 repository](https://sourcecode.socialcoding.bosch.com/projects/BCAI/repos/bcai-training-deeplearning-overview) to train a model for lane keeping
* Follow the instructions detailed in the [RemoCar AI repository](https://sourcecode.socialcoding.bosch.com/projects/BCAI/repos/bcai-remocar-ai) to run the model on the RemoCar

## Raspberry Pi Serial connection setup
* Add "dtoverlay=pi3-disable-bt" to /boot/config.txt
* Remove "console=serial0,115200" from /boot/cmdline.txt
* Shutdown pi completely, remove power and reboot

## Assembly of the 3D printed and electronic parts 
After the tamiya remote controlled car has been assembled (without the cover), it is time to attach the 3D printed and electronic parts.
In the following, an overview of the parts and screws that we have used is given. However, other screws might work as well.
The remocar consists of the following parts:


| Letter | Part | Quantity |Material required (per unit) |
| ------| ------ | ------ |------ |
| A| Sidepart | 2 |M3x16 cylinder screw (2x), matching nut(1x) |
| B| Base | 1 |2.9x16 sheet-metal screw (DIN 7982) (4x) |
| C| Battery | 1 |None |
| D| Battery Cover | 1 |2.9x13 sheet-metal screw (DIN 7982) (4x) | 
| E| Raspberry Pi 3 | 1 |2.9x9.5 sheet-metal screw (DIN 7982) (4x) |
| F| Arduino Uno | 1 |2.9x9.5 sheet-metal screw (DIN 7982) (4x) |
| G| Breadboard | 1 |None | 
| H| Hall Sensor Mount | 2 |M2x6 cylindric screws (2x) + matching nuts, M3x8 cylindric screw (1x) |
| I| Hall Sensor | 2 | None | 
| J| Magnet Rim | 2 |None, instant glue optional, washer (Unterlegscheibe) optional |
| K| Magnets | 16 | Instanst glue |
| L| Camera | 1 |2.9x6.5 sheet-metal screw (DIN 7982) (2x)  |
| M| Camera Mount | 1 | M3x16 counter-sunk screw (4x) + nuts, M3x10 counter-sunk screw (2x) + nuts, M4x20 cylindric screw (2x) + nuts |

### Preparations
Before the assembly can start, we need to take care of our tyres.
* Glue the magnets (K) into the corresponding slots of the rim (J). Make sure to push the magnets towards the center of the circle as far as possible.
Also make sure that the orientation is correct! The hall sensor can only detect a pulse if a magnet is oriented the right way. 
You can check the orientation of the magnets by hooking up the hall sensor to the arduino and holding a magnet in front of it.
If the magnet is correctly oriented, the red LED will light up.
* Afterwards, push the rim that holds the magnets (J) into the inner wheel rim of the tamiya car. If necessary, use instant glue.

### Assembly Instructions
* Attach (A) to the side of the vehicle. Use the screw with the nut for the front hole, the screw wtithout the nut for the back hole (Use the upper hole of the two available holes).
* Repeat on the other side.
* Place (B) on the two sideparts (A). The holes should match. Attach (B).
* Place the battery (C) in its cage.
* Attach the battery cover (D).
* Attach (E), (F) and (G).
* Mounting the hall sensor is a bit tricky: Screw the two M2x6 screws into (H). 
* Use the M3x8 screw to attach (H) to the chassis of the car.
* Place (I) on (H) and use two nuts to fasten the sensor (I).
* Make sure the sensor's distance to the magnets is close enough to detect the pulses.
* Repeat on the other side.
* Mounting the camera is also a bit tricky:
* First, place the camera (L) within the case and attach it using the two sheet-metal screws.
* Then, close the case and attach the joints using the four M3x16 screws.
* Afterwards, attach the U-shaped mount to the base using the M4 screws.
* Finally, attach the camera case to the mount using the two M3x10 screws and matching nuts.
