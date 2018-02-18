#!/usr/bin/env python

# Import the python time module
import time

# Define "dictionary" for the "Text-Clock"
dict_text_clock={}

def init():
    """Opens the file Uhrprojekt_Zeitanzeige_Zeitansage.csv
    and read the key-value-pair to store the clock text into the ditctionary
    dict_text_clock.
    """
    with open("textclock_timetext_DE_de.csv", encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n", "")
            (key,val) = line.split(",")
            dict_text_clock[key] = val

def get_text_time(hour, minute):
    """ Make out of hour and minute a readable text.
    hour:    hours in range 0..23
    minutes: minutes in range 0..59 """

    # Build the "key". Take care abut the pre-leading zeros for the hours and minutes.
    hour   = hour%24    # Use modulo to accept mistaken inputs above 23 hours.
    minute = minute%60  # Use modulo to accept mistaken inputs above 59 minutes.
    minute = minute - minute%5 # This ensures the five-minutes time-step.
    dict_text_clock_key = "{0:02d}:{1:02d}".format(hour, minute)
    #print(dict_text_clock_key

    # Return the clock text from the dictionary.
    return dict_text_clock[dict_text_clock_key]


# MAIN PROGRAN

def main():
    """ Print the actual time to the console output."""
    # Initialize dictionary
    init()

    # This is the endless loop to print out the actual time.
    while True:
        # Get the current, real time for the local timezone.
        currentLocalTime=time.localtime()

        # Print the  current local time.
        print(get_text_time(currentLocalTime.tm_hour, currentLocalTime.tm_min))

        # Calculate the duration until the next 'Bang' aligned to five minutes steps.
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
