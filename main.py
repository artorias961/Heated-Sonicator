from machine import Pin

def user_interface_prompt():
    # Prompting the user to input the time for how long the machine should run
    print("Input the hr/mm for the machine to run")
    
    # Button one will toggle between hr/mm (NOT DEFINE PIN)
    toggle_button = Pin(13, Pin.IN)
    
    # Button 2 will increment the time (NOT DEFINE PIN)
    increment_time_button = Pin(14, Pin.IN)
    
    # Button 3 will decrement the time (NOT DEFINE PIN)
    decrement_time_button = Pin(15, Pin.IN)
    
    # Button 4 will start the machine(NOT DEFINE PIN)
    set_button = Pin(16, Pin.IN)
    
    # Creating a while loop for the user to input there time
    while True:
        # Creating a temp button for a frequncy response
        temp = 0
        hour = 0
        minutes = 0
        
        # This will be regarding for hour
        # if temp == 0 && toggle_button.value() == 0:
        
        # Creating an if statement to increase the hour
        if increment_time_button.value() > 0 and decrement_time_button ==0:
            hour = hour + 1
        # Creating an if statement to drease the hour
        if decrement_time_button.value() > 0 and increment_time_button == 0:
            hour = hour - 1
        # 
        if hour < 0:
            print("The value has to be great than 0 !!!")
            print("We have increase the hour by 1")
            hour = hour + 1
        if hour >= 9:
            print("You have exceeded the maximum hours, lower your hours")
            print("We have decrease the hour by 1")
            hour = hour - 1
        



def main():
    user_interface_prompt()