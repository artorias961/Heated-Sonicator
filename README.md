# Heated-Sonicatormain
- Repairing the water bath for ECST makerspace,
  used to dissolve supports on ABS 3D prints
- Microcontroller was fried and obsolete, replacing with a ESP32 Feather
  https://www.adafruit.com/product/5400
  
  
Rough Flow Chart
![image](https://user-images.githubusercontent.com/12043783/196532078-3c4a2dbf-a773-4274-a81c-dd474326b43c.png)











# Set up for ESP32

We are going to show you how to install MicroPython and CircuitPython. MicroPython is a python base but made for microcontroller. While CircuitPython is a derivative for MicroPython and AdaFruit uses this for python base microcontroller. ESP32 comes in default using C language however, we have decided to use python base for its simplicity and helping other students to get a better grasp of the code. We prefer C but it will help out in the future for others to understand the code.



#### Flashing MicroPython for ESP32
You are going to need the firmware to change your ESP32 from C to MicroPython. If you do not have the firmware then look at the reference's to find the firmware for this board. We are going to need to erase everything inside of the ESP32 board then flash it with MicroPython. Once we flashed the board then we are going to check if the board can be recognize by the [Thonny IDE](https://thonny.org).


What worked for me is using [mambaforge](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html). Install mambaforge or find something that works for you, then use the following command:

```Python
pip install esptool
```

Once you have installed the package, ***check your device manager to determine which port your ESP32 is connected to***, once you find it then get the number and input the following to mambaforge or whatever you are using (*Change # to your number*):

```Python
esptool -p COM# flash_id
```
A command line should prompt up and tell you what board is your ESP32 is. We are then going to erase everything inside of the ESP32 board, do the following (*Change # to your number*):

```Python
esptool --chip esp32 --p COM# erase_flash
```

Go to your directory of the firmware file you installed then from mambaforge, do the following command (*Change # to your number*):

```Python
esptool --chip esp32 --p COM# write_flash -z 0x1000 whateverYourFirmwareFileNameIs.bin
```





#### Flashing CircuitPython for ESP32

You are going to need the firmware to change your ESP32 from C to CircuitPython. If you do not have the firmware then look at the reference's to find the firmware for this board. We are going to need to erase everything inside of the ESP32 board then flash it with MicroPython. Once we flashed the board then we are going to check if the board can be recognize by the [Thonny IDE](https://thonny.org).

What worked for me is using [mambaforge](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html). Install mambaforge or find something that works for you, then use the following command:

```Python
pip install esptool
```

Once you have installed the package, ***check your device manager to determine which port your ESP32 is connected to***, once you find it then get the number and input the following to mambaforge or whatever you are using (*Change # to your number*):

```Python
esptool -p COM# flash_id
```
A command line should prompt up and tell you what board is your ESP32 is. We are then going to erase everything inside of the ESP32 board, do the following (*Change # to your number*):

```Python
esptool --chip esp32 --p COM# erase_flash
```

Go to your directory of the firmware file you installed then from mambaforge, do the following command (*Change # to your number*):

```Python
esptool --chip esp32 --p COM# write_flash -z 0x0000 whateverYourFirmwareFileNameIs.bin
```

To change the following in Thonny IDE, you need to change the interpreter settings and you are ready.

<p align="center">
<img src="https://user-images.githubusercontent.com/54751574/199360982-3f4492b2-efee-4112-a028-1c656bd4d050.png">
</p>





#### Verifying the firmware using Thonny IDE 

Open Thonny and you should get the following prompt:



<p align="center">
<img src="https://user-images.githubusercontent.com/54751574/199181008-79ed1aeb-2123-44ab-b2ef-cf49d6b621f6.png">
</p>


Go to **Run** then click **Configure interpreter. . .**


<p align="center">
<img src="https://user-images.githubusercontent.com/54751574/199181290-eadb9055-97e3-4947-8c28-234736a7a043.png">
</p>

Now go to **Interpreter**, find the prompt *Which kind of interpreter should Thonny use for running your code?*. Now select **MicroPython (ESP32)**, then click ok 


<p align="center">
<img src="https://user-images.githubusercontent.com/54751574/199181709-76888865-0eca-4028-b6f5-06838161b257.png">
</p>

Connect your ESP32 Feather V2 board and press the reset button. You should get the following:



<p align="center">
<img src="https://user-images.githubusercontent.com/54751574/199182112-7b61bbda-19b8-42c9-be02-256299a74da5.png">
</p>


# ESP32 Pin Layout


<p align="center">
<img src="https://user-images.githubusercontent.com/54751574/201508138-0a738ecb-21a5-4301-bf9b-e8b0466828f9.png">
</p>


# Reference
- MicroPython 
  - [MicroPython Firmware for Feather ESP32](https://micropython.org/download/esp32spiram/)
  - [Reference how to setup MicroPython using ESP32](https://learn.adafruit.com/adafruit-esp32-feather-v2/micropython-setup)
  - [OLED I2C Reference](https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html)
  - [Basic I2C Commands](https://docs.micropython.org/en/latest/library/machine.I2C.html)
  - [ESP32 MicroPython API](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
 
- CircuitPython 
  - [CircuitPython](https://circuitpython.org/board/adafruit_feather_esp32_v2/)
  - [Reference how to setup CircuitPython using ESP32](https://learn.adafruit.com/circuitpython-with-esp32-quick-start/command-line-esptool)
  - [ESP32 CircuitPython API](https://docs.circuitpython.org/en/latest/ports/espressif/README.html)
  - [Link for what is CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython)
  - [General Link for CircuitPython](https://docs.circuitpython.org/en/latest/README.html)
  - [CircuitPython API](https://docs.circuitpython.org/en/latest/shared-bindings/index.html)
  - [Setup Web Workflow](https://learn.adafruit.com/circuitpython-with-esp32-quick-start/setting-up-web-workflow)
  
- ESP32/ESP8266
  - [Information about ESPTOOL](https://docs.espressif.com/projects/esptool/en/latest/esp32/index.html#quick-start)
  - [ESP32 V2 Pin Layout](https://learn.adafruit.com/adafruit-esp32-feather-v2/pinouts)


