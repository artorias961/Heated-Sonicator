# Heated-Sonicatormain
- Repairing the water bath for ECST makerspace,
  used to dissolve supports on ABS 3D prints
- Microcontroller was fried and obsolete, replacing with a ESP32 Feather
  https://www.adafruit.com/product/5400
  
  
Rough Flow Chart
![image](https://user-images.githubusercontent.com/12043783/196532078-3c4a2dbf-a773-4274-a81c-dd474326b43c.png)















# Flashing MicroPython for ESP32
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

### Verifying the firmware using Thonny IDE 

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


# Flashing MicroPython for CircuitPython

You are going to need the firmware to change your ESP32 from C to CircuitPython. If you do not have the firmware then look at the reference's to find the firmware for this board. We are going to need to erase everything inside of the ESP32 board then flash it with MicroPython. Once we flashed the board then we are going to check if the board can be recognize by the [Thonny IDE](https://thonny.org).

What worked for me is using [mambaforge](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html). Install mambaforge or find something that works for you, then use the following command:


### Reference
- [MicroPython Firmware for Feather ESP32](https://micropython.org/download/esp32spiram/)
- [CircuitPython](https://circuitpython.org/board/adafruit_feather_esp32_v2/)
- [OLED I2C Reference](https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html)
- [Basic I2C Commands](https://docs.micropython.org/en/latest/library/machine.I2C.html)
- [ESP32 MicroPython API](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
- [Information about ESPTOOL](https://docs.espressif.com/projects/esptool/en/latest/esp32/index.html#quick-start)

