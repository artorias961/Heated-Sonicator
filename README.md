# Heated Sonicator – ESP32 CCA Replacement



<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/3e6eb601-3665-46d4-aff3-c9edcdbcae96" />














## Overview
This repository documents the **replacement of the original CCA (Circuit Card Assembly)** of a **heated ultrasonic water bath (sonicator)** with an **ESP32-based controller**.

The original control board failed and was either obsolete or not economically repairable.  
The solution was to **retrofit the system using an ESP32 Feather**, restoring functionality while making the system easier to maintain, modify, and debug.

This project was completed in a makerspace environment where the heated sonicator is primarily used to **dissolve ABS support material** from 3D-printed parts.



## Primary Purpose of This Repository
The **main reason this repository exists** is to:

> **Replace the original heated sonicator CCA with an ESP32 board**

Specifically:
- Remove the failed proprietary control electronics
- Install an ESP32 Feather as the new controller
- Re-implement heater control and system logic in Python (MicroPython / CircuitPython)
- Provide documentation so the repair can be reproduced or maintained by others



## System Architecture

![image](https://user-images.githubusercontent.com/12043783/196532078-3c4a2dbf-a773-4274-a81c-dd474326b43c.png)

**High-level flow:**
- ESP32 handles logic and control
- Power board switches heater and ultrasonic elements
- Sensors provide temperature feedback
- Firmware enforces safe operation



## Repository Structure

```
Heated-Sonicator/
├── main.py                      # ESP32 main application
├── Lib/                          # Supporting libraries for MicroPython/CircuitPython
├── PowerBoard/                   # Heater / power electronics documentation
├── Useful_files_for_debugging/   # Debug notes, helpers, and references
├── Hannah Consult 10_11.pdf       # Design / consultation reference
└── README.md
```



## ESP32 Setup

This project uses an **Adafruit ESP32 Feather** running either **MicroPython** or **CircuitPython**.

### Flashing Firmware
Example using `esptool`:

```bash
esptool.py --chip esp32 erase_flash
esptool.py --chip esp32 write_flash -z 0x1000 firmware.bin
```

### Development Environment
- **Thonny IDE**
- USB serial connection to ESP32
- Python-based workflow for fast iteration

<p align="center">
<img src="https://user-images.githubusercontent.com/54751574/199360982-3f4492b2-efee-4112-a028-1c656bd4d050.png">
</p>








<p align="center">
<img src="https://user-images.githubusercontent.com/54751574/199181008-79ed1aeb-2123-44ab-b2ef-cf49d6b621f6.png">
</p>




<p align="center">
<img src="https://user-images.githubusercontent.com/54751574/199181290-eadb9055-97e3-4947-8c28-234736a7a043.png">
</p>



<p align="center">
<img src="https://user-images.githubusercontent.com/54751574/199181709-76888865-0eca-4028-b6f5-06838161b257.png">
</p>




<p align="center">
<img src="https://user-images.githubusercontent.com/54751574/199182112-7b61bbda-19b8-42c9-be02-256299a74da5.png">
</p>




<p align="center">
<img src="https://user-images.githubusercontent.com/54751574/201508138-0a738ecb-21a5-4301-bf9b-e8b0466828f9.png">
</p>



## Firmware Entry Point

- `main.py` is the primary runtime file
- Executed automatically on boot
- Responsible for:
  - Heater enable/disable
  - Temperature monitoring
  - Safety checks
  - System state control



## Power Electronics

![Power Board](images/power_board.png)

The `PowerBoard/` directory contains documentation related to:
- Heater switching
- Isolation considerations
- Power handling
- Safety constraints

⚠️ **Warning:** This system controls mains-level power.  
Only qualified individuals should modify or service the power electronics.


## Debugging & Maintenance

The `Useful_files_for_debugging/` folder includes:
- Test notes
- Reference commands
- Bring-up helpers
- Troubleshooting information

These files were used during commissioning of the ESP32-based replacement CCA.



## Status

✔ Heated sonicator successfully restored  
✔ Original CCA fully replaced by ESP32  
✔ System operational and serviceable  

Future improvements may include:
- PID temperature control
- Display/UI integration
- Data logging
- Safety watchdogs

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

## License
This repository is intended for **educational, maintenance, and makerspace use**.

Use at your own risk.































