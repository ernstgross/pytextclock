import RPi.GPIO as GPIO
import time

"""
In this project we use the raspberry-pi PIN layout as described in the next lines:

PIN 01   3.3V          not used           PIN 02   5V             not used
PIN 03   GPIO-02/I2C   LED-00             PIN 04   5V             not used
PIN 05   GPIO-03/I2C   LED-01             PIN 06   GND            not used
PIN 07   GPIO-04       LED-02             PIN 08   GPIO-14/UART   LED-03
PIN 09   GND           not-used           PIN 10   GPIO-15/UART   LED-04
PIN 11   GPIO-17       LED-05             PIN 12   GPIO-18        LED-06
PIN 13   GPIO-27       LED-07             PIN 14   GND            not used
PIN 15   GPIO-22       LED-08             PIN 16   GPIO-23        LED-09
PIN 17   3.3V          not used           PIN 18   GPIO-24        LED-10
PIN 19   GPIO-10/SPI   not used           PIN 20   GND            not used
PIN 21   GPIO-09/SPI   not used           PIN 22   GPIO-25        LED-11
PIN 23   GPIO-11/SPI   not used           PIN 24   GPIO-08/SPI    not used
PIN 25   GND           not used           PIN 26   GPIO-07/SPI    not used
PIN 27   DNC           not used           PIN 28   DNC            not used
PIN 29   GPIO-05       LED-12             PIN 30   GND            not used
PIN 31   GPIO-06       LED-13             PIN 32   GPIO-12        LED-14
PIN 33   GPIO-13       LED-15             PIN 34   GND            not used
PIN 35   GPIO-19       LED-16             PIN 36   GPIO-16        LED-17
PIN 37   GPIO-26       LED-18             PIN 38   GPIO-20        LED-19
PIN 39   GND           used as GND        PIN 40   GPIO-21        not used
"""

__version__    = '0.1.1'
__author__     = 'Ernst Gross'
__email__      = "ernst@grossmusik.de"
__copyright__  = "Copyright 2018, The pyclocktext project"
__credits__    = ["Joachim Gross","Johannes Gross"]
__license__    = "MIT"
__status__     = "Development"

out_pin_list = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 35, 36, 37, 38]
out_pin_list_len = len(out_pin_list)


def init_out_pin_list():
    """Init leds to off"""
    GPIO.setmode(GPIO.BOARD)

    for pin in out_pin_list:
        GPIO.setup ( pin, GPIO.OUT)
        GPIO.output( pin, GPIO.LOW)

    return out_pin_list_len

def cleanup():
    """Cleanup this module. 
    This function is intended to be used if the programm was not terminated correctly.
    Then the GPIO modules are not cleaned up. Therefore this function can be called at the begin or at the end.
    """
    GPIO.cleanup()

def set_clock_leds(clock_led_ids):
    """Set the clock LEDs in the clock_led_ids to ON (high)"""
    print(clock_led_ids)

    # First set all LED's to OFF (low)
    for index in range(out_pin_list_len):
        GPIO.output(out_pin_list[index-1],GPIO.LOW )

    for led_id in range(len(clock_led_ids)):
        GPIO.output(out_pin_list[ clock_led_ids[led_id] ],GPIO.HIGH)
        print(clock_led_ids[led_id])


def main():
    """Main programm"""
    print("This is the LED text-clock project")
    print("We run the test sequence forward and backward over all 20 LED's for 10 times")

    init_out_pin_list()

    durationOn  = 0.1
    durationOff = 0.1
    pause = 0.5

    for x in range(10):
        print("Sequence", x)

        # Set every single LED on and of in a forward direction.
        for index in range(out_pin_list_len):
            GPIO.output(out_pin_list[index  ],GPIO.HIGH)
            GPIO.output(out_pin_list[index-1],GPIO.LOW )
            time.sleep(pause)

        time.sleep(durationOn)

        # Set every single LED on and of in a backward direction.
        for index in range(out_pin_list_len):
            nextLed = (out_pin_list_len - 1) - index
            prevLed = (out_pin_list_len - index) % out_pin_list_len
            #print(index, nextLed, prevLed)
            GPIO.output(out_pin_list[nextLed],GPIO.HIGH)
            GPIO.output(out_pin_list[prevLed],GPIO.LOW)
            time.sleep(pause)

        time.sleep(durationOn)

    cleanup()

    print("End of programm")

# If this module is used as a standalone application
if __name__ == '__main__':
    main()
