#!/usr/bin/env python

# Import the python time module
import time
import blinkled

# Define "dictionary" for the "Text-Clock"
dict_time_to_text = {}
dict_text_hours_to_led = {}
dict_text_minutes_to_led = {}
dict_text_minutes_separator_to_led = {}

base_directory = "/home/pi/github/pytextclock/"

def init_text_to_led():
    """Opens the files
    textclock_text-hours_to_led_DE-de.csv
    textclock_text-minutes_to_led_DE-de.csv
    textclock_text-minutes-separator_to_led_DE-de.csv
    and read the key-value-pair to store the led-identifier for each clock text element
    into the ditctionary dict_key_time_to_val_text.
    
    fünf    [0] zehn  [1] und [2]
    zwanzig [3] vor   [4]
    halb    [5] nach  [6]
    eins    [7] zwei  [8]
    drei    [9] vier [10]
    fünf   [11] sechs[12]
    sieben [13] acht [14]
    neun   [15] zehn [16] elf [17]
    zwölf  [18] null [19]
    """
    with open(base_directory + "textclock_text-hours_to_led_DE-de.csv", encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.replace(" ", "")
            (key,val) = line.split(",")
            dict_text_hours_to_led[key] = int(val)
            #print(key,val)

    with open(base_directory + "textclock_text-minutes_to_led_DE-de.csv", encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.replace(" ", "")
            (key,val) = line.split(",")
            dict_text_minutes_to_led[key] = int(val)
            #print(key,val)
    
    with open(base_directory + "textclock_text-minutes-separator_to_led_DE-de.csv", encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.replace(" ", "")
            (key,val) = line.split(",")
            dict_text_minutes_separator_to_led[key] = int(val)
            #print(key,val)

def init_time_to_text():
    """Opens the file textclock_timetext_DE_de.csv
    and read the key-value-pair to store the clock text into the ditctionary
    dict_key_time_to_val_text.
    """
    with open(base_directory + "textclock_timetext_DE-de.csv", encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n", "")
            (key,val) = line.split(",")
            dict_time_to_text[key] = val
            
def init():
    """Init all sub init routines.
    """
    init_time_to_text()
    init_text_to_led()

def is_minute_separator_in(text):
    """Check for Minute-Separator in the text argument.
    """
    for separator in text.split(" "):
        #print(separator, text)
        if(separator in dict_text_minutes_separator_to_led):
            return True
    
    return False

def get_minute_separator(text):
    """Returns the minute separator out of the text argument.
    """
    for separator in text.split(" "):
        #print(separator, text)
        if(separator in dict_text_minutes_separator_to_led):
            return separator
    
    return ""
    
def split_minutes_text_to_search(minutes_text_to_search):
    """Split the minutes_text_to_search into single words.
    """
    new_list_of_minutes_text_to_search = []
    
    for key in dict_text_minutes_to_led.keys():
        if(key in minutes_text_to_search):
            new_list_of_minutes_text_to_search.append(key)

    #print(minutes_text_to_search)
    #print(new_list_of_minutes_text_to_search)
    return new_list_of_minutes_text_to_search;

def get_leds_from_text(text):
    """Returns the identifier numbers of the needed LED's
    to enlighten the text-fields of the dispaly the text
    """
    leds=[]
    
    if(is_minute_separator_in(text)):
        minute_separator = get_minute_separator(text)
        minutes_text_to_search = text.split(minute_separator)[0].replace(" ","")
        hours_text_to_search   = text.split(minute_separator)[1].replace(" ","")
        
        # Look for minutes
        minutes_text_to_search = split_minutes_text_to_search(minutes_text_to_search)
        for minutes_text in minutes_text_to_search:
            leds.append(dict_text_minutes_to_led[minutes_text])
        
        # Look for seperator
        leds.append(dict_text_minutes_separator_to_led[minute_separator])
        
        # Look for hours
        leds.append(dict_text_hours_to_led[hours_text_to_search])
        
    else:
        # Look for hours only
        for hour_text in text.split(" "):
            leds.append(dict_text_hours_to_led[hour_text])
    
    return leds

def get_text_time(hour, minute):
    """ Make out of hour and minute a readable text.
    hour:    hours in range 0..23
    minutes: minutes in range 0..59 """

    # Build the "key". Take care abut the pre-leading zeros for the hours and minutes.
    hour   = hour%24    # Use modulo to accept mistaken inputs above 23 hours.
    minute = minute%60  # Use modulo to accept mistaken inputs above 59 minutes.
    minute = minute - minute%5 # This ensures the five-minutes time-step.
    dict_key_time_to_val_text_key = "{0:02d}:{1:02d}".format(hour, minute)
    #print(dict_key_time_to_val_text_key

    # Return the clock text from the dictionary.
    return dict_time_to_text[dict_key_time_to_val_text_key]
 

# MAIN PROGRAN

def main():
    """ Print the actual time to the console output."""
    # Initialize dictionary
    init()
    blinkled.init_out_pin_list()

    # This is the endless loop to print out the actual time.
    while True:
        # Get the current, real time for the local timezone.
        currentLocalTime=time.localtime()

        # Print the current local time as text.
        clocktext = get_text_time(currentLocalTime.tm_hour, currentLocalTime.tm_min)
        print(clocktext)
      
        # Print the used LED's for the current local.
        clock_led_ids = get_leds_from_text(clocktext)
        print("LED's:",clock_led_ids)
        blinkled.set_clock_leds(clock_led_ids)

        # Calculate the duration until the next 'Bang' occurs every five minutes.
        delta_minutes_to_sleep =  4 - currentLocalTime.tm_min%5
        delta_seconds_to_sleep = 60 - currentLocalTime.tm_sec
        delta_seconds_sum_to_sleep = delta_minutes_to_sleep*60 + delta_seconds_to_sleep

        # Debug-Information for test (can be uncommented for final release.)
        print("\t\tCurrent local time: " + time.asctime())
        print("\t\tI will sleep for "+str(delta_minutes_to_sleep)+" minutes and "+str(delta_seconds_to_sleep)+" seconds (in sum "+ str(delta_seconds_sum_to_sleep)+" seconds) until the next 'Bang'")

        # Sleep until the next "Bang"
        time.sleep(delta_seconds_sum_to_sleep)

# If this module is used as a standalone application
if __name__ == '__main__':
    main()
