import board
import time
import displayio
from digitalio import DigitalInOut, Direction, Pull 
import terminalio
import adafruit_ahtx0
from adafruit_display_text import label
import adafruit_displayio_sh1107

def temp_and_humidity():
    # Use for I2c for Temp/Humidity sensor
    i2c = board.I2C()
    sensor = adafruit_ahtx0.AHTx0(i2c)
    
    # Getting the temperature from the sensor
    temperature = sensor.temperature
    
    # Getting the humidity from the sensor 
    humidity = sensor.relative_humidity
    
    # Convert datatype from float to int
    temperature = int(temperature)
    humidity = int(humidity)
    
    return temperature, humidity
    

def display(temp: int, humid: int):
    
    # Calling the OLED screen
    displayio.release_displays()

    # Use for I2C for LCD
    i2c = board.I2C()
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

    # SH1107 is vertically oriented 64x128
    WIDTH = 128
    HEIGHT = 64
    BORDER = 2

    # Setting up the configuration for the display
    display = adafruit_displayio_sh1107.SH1107(
        display_bus,     # I2C bus
        width=WIDTH,     # Max Width
        height=HEIGHT,   # Max height
        rotation=0)      # No rotation

    # Make the display context
    splash = displayio.Group()
    display.show(splash)

    # Setting up the color bits for the OLED Display (Color format)
    color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF  # White Pixels

    # Creating the outline box on the OLED Display
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)

    # Draw a smaller inner rectangle in black
    inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black
    inner_sprite = displayio.TileGrid(
        inner_bitmap,
        pixel_shader=inner_palette,
        x=BORDER,
        y=BORDER)
    splash.append(inner_sprite)

    # Draw some label text
    text1 = "   Arty Chan T-T"
    text_area = label.Label(terminalio.FONT,  # font style
                            text=text1,       # text string
                            scale=1,          # font size
                            color=0xFFFFFF,   # white pixels
                            x=8,              # x-axis position
                            y=8               # y-axis position
                            )                 
    
    splash.append(text_area)
    text2 = f"Temperature: {temp}C\nHumidity: {humid}%"
    text_area2 = label.Label(
        terminalio.FONT, # font style
        text=text2,      # text string
        scale=1,         # font size
        color=0xFFFFFF,  # white pixel
        x=9,             # x-axis position
        y=20             # y-axis position
    )
    splash.append(text_area2)
    
def led_setup(temp):
    # Pin setup for overload water level
    water_level_overload_led = DigitalInOut(33)
    water_level_overload_led.direction = digitalio.Direction.OUTPUT
    
    # Pin setup for underload water level
    water_level_underload_led = DigitalInOut(15)
    water_level_underload_led.direction = digitalio.Direction.OUTPUT
    
    # Pin setup for max temperature limit
    max_temp_led = DigitalInOut(32)
    max_temp_led.direction = digitalio.Direction.OUTPUT
    
    return water_level_overload_led, water_level_underload_led, max_temp_led

def water_level_status_led(temp, humid, water_level_overload_led, water_level_underload_led, max_temp_led):
    # Checking for the temperature limit 
    if 70 > temp:
        max_temp_led.value = True
        stop_switch = True
        
    return stop_switch
        
        
def main():
    # Setting up the pins
    water_level_overload_led, water_level_underload_led, max_temp_led = led_setup()
    
    # Infinite Statement
    while True:
        # Getting the updated temperature and humidity sensor data
        temp, humid = temp_and_humidity()
        
        # Testing to see if the code works and prints on the computer console 
        print(f"Temp: {temp} C, Humid: {humid} %")
        
        # Waits for 2 mili-seconds for the data
        time.sleep(2)
        
        # Send the data to the display oled module
        display(temp, humid)
        
        # Send the pins and the sensor data to check 
        stop_switch = water_level_status_led(temp, humid, water_level_overload_led, water_level_underload_led, temp_overload_led)
        
        # Waits for 2 mili-seconds for the data 
        time.sleep(2)
        
        if !(stop_switch):
            break
    

