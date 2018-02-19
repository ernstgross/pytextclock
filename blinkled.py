import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

out_pin_list = [7, 11, 13, 15]

for pin in out_pin_list:
    GPIO.setup ( pin, GPIO.OUT)
    GPIO.output( pin, GPIO.LOW)

durationOn  = 0.1
durationOff = 0.1
pause = 0.2

for x in range(10):
    for index in range(4):
        GPIO.output(out_pin_list[index],GPIO.HIGH)
        GPIO.output(out_pin_list[index-1],GPIO.LOW)
        time.sleep(pause)

    time.sleep(durationOn)

    for index in range(4):
        nextLed = 3-index
        prevLed = (3-index+1)%4
        print(index, nextLed, prevLed)
        GPIO.output(out_pin_list[nextLed],GPIO.HIGH)
        GPIO.output(out_pin_list[prevLed],GPIO.LOW)
        time.sleep(pause)

    time.sleep(durationOn)

GPIO.cleanup()


