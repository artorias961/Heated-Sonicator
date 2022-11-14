import board
import time
import displayio
from digitalio import DigitalInOut, Direction, Pull 
import terminalio
import adafruit_ahtx0
from adafruit_display_text import label
import adafruit_displayio_sh1107
import microcontroller
    

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


def led_setup():
    """
    Setup the pin then return in when needed for another function
    """
    # Pin setup for overload water level (Water Level Transducer)
    pin33 = board.D33
    water_level_overload_led = DigitalInOut(pin33)
    water_level_overload_led.direction = Direction.OUTPUT
    
    # Pin setup for underload water level (Water Level Transducer)
    pin15 = board.D15
    water_level_underload_led = DigitalInOut(pin15)
    water_level_underload_led.direction = Direction.OUTPUT
    
    # Pin setup for max temperature limit
    pin32 = board.D32
    max_temp_led = DigitalInOut(pin32)
    max_temp_led.direction = Direction.OUTPUT
    
    return water_level_overload_led, water_level_underload_led, max_temp_led


def button_setup():
    # Pretend this is the water level transducer
    pin14 = board.D14
    button_one = DigitalInOut(pin14)
    button_one.direction = Direction.INPUT
    button_one.pull = Pull.UP
    
    # Pretend this is the water level transducer
    pin27 = board.D27
    button_two = DigitalInOut(pin27)
    button_two.direction = Direction.INPUT
    button_two.pull = Pull.UP
    
    # To increase the time
    pin12 = board.D12
    button_three = DigitalInOut(pin12)
    button_three.direction = Direction.INPUT
    button_three.pull = Pull.UP
    
    # To decrease the time
    pin13 = board.D13
    button_four = DigitalInOut(pin13)
    button_four.direction = Direction.INPUT
    button_four.pull = Pull.UP
    
    # Select button (pin number may give issues)
    pin5 = board.D5
    button_five = DigitalInOut(pin5)
    button_five.direction = Direction.INPUT
    button_five.pull = Pull.UP
    
    return button_one, button_two, button_three, button_four, button_five
    


def water_level_status_led(temp, humid, water_level_overload_led, water_level_underload_led, max_temp_led, button_one, button_two):
    # Checking for the temperature limit
    if temp > 70:
        max_temp_led.value = True
        time.sleep(1)
        stop_switch = True
    else:
        max_temp_led.value = False
        stop_switch = False
    
    # If the high level is met then turn on led and kill the machine
    if button_one.value and (not button_two.value):
        print("Warning high water level. Machine will stop")
        water_level_overload_led.value = True
        time.sleep(1)
        stop_switch = True
    else:
        water_level_overload_led.value = False
        stop_switch = False
        
    # If the low level is met then turn on led and kill the machine
    if button_two.value and (not button_one.value):
        print("Warning low water level. Machine will stop")
        water_level_underload_led.value = True
        time.sleep(1)
        stop_switch = True
    else:
        water_level_underload_led.value = False
        stop_switch = False
    
    return stop_switch


def get_pin_info():
    """
    Prints out information of the pin name. Meant to call the correct pin name
    """
    board_pins = []
    for pin in dir(microcontroller.pin):
        if isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin):
            pins = []
            for alias in dir(board):
                if getattr(board, alias) is getattr(microcontroller.pin, pin):
                    pins.append("board.{}".format(alias))
            if len(pins) > 0:
                board_pins.append(" ".join(pins))
    for pins in sorted(board_pins):
        print(pins)


def set_clock_timer(button_three, button_four, button_five):
    # Asking the user to input a time (by hour)
    user_clock_input = 0
    
    # A switch to break the while loop
    clock_done_switch = False
    
    while not clock_done_switch:
        # Print to the OLED
        
        # Increase the timer 
        if button_three.value > 0:
            user_clock_input += 1
        # Decrease the timer
        elif button_four.value > 0:
            user_clock_input -= 1
        
        # Checking if the clock timer is within range
        if (user_clock_timer < 0):
            # Increase the timer by one hour 
            user_clock_timer += 1
            
            # Print in the OLED screen
            print("Warning you have passed the limit")
            print("Increasing the timer by 1 hour")
        
        # Checking if the clock timer is within range
        elif (user_clock_timer > 8):
            # Decreasing the timer by one hour
            user_clock_timer -= 1
            
            # Print on the OLED screen
            print("Warning you have passed the limit")
            print("Decreasing the timer by 1 hour")
        
        # If user is done, then press the button to break the while loop
        if button_five.value > 0:
            clock_done_switch = True
        
        # Print on the OLED screen of the current timer 
        print(user_clock_timer)
    
    return user_clock_timer 

def clock_timer():
    pass

def main():
    # Setting up the pins
    water_level_overload_led, water_level_underload_led, max_temp_led = led_setup()
    
    # Setting up the buttons and transducer
    button_one, button_two, button_three, button_four, button_five = button_setup()
    
    # Set clock timer
    timer = set_clock_timer(button_three, button_four, button_five)
    
    # Infinite Statement
    while True:
        # Getting the updated temperature and humidity sensor data
        temp, humid = temp_and_humidity()
        
        # Testing to see if the code works and prints on the computer console 
        print(f"Temp: {temp} C, Humid: {humid} %")
        print(button_one.value)
        print(button_two.value)
        
        # Send the data to the display oled module
        display(temp, humid)
        
        # Send the pins and the sensor data to check 
        stop_switch = water_level_status_led(temp,
                                             humid,
                                             water_level_overload_led,
                                             water_level_underload_led,
                                             max_temp_led,
                                             button_one,
                                             button_two)
        
        # Clock timer counting down 
        stop_switch = clock_timer()
        
        # Waits for 1 mili-seconds for the data 
        time.sleep(1)
        
        if stop_switch:
            break
    



