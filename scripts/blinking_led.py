#!/usr/bin/env python3
import RPi.GPIO as GPIO # pin lib for the Raspberry
import time
ledPin = 18 # the BCM pin connected to the LED

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
'''
while True:
    print("Led ON...")
    GPIO.output(18, True)
    time.sleep(1)
    print("Led OFF...")
    GPIO.output(18, False)
    time.sleep(1)

'''
def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    # Set ledPin's mode to output and inital level to High(3.3v)
    GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.HIGH)

# Define a main function for main process
def main():
    while True:
        print("Led OFF...")
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(1)

        print("Led ON...")
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(1)

# Cleanup function
def destroy():
    print("Led OFF...")
    GPIO.output(ledPin, GPIO.LOW)
    # Release resources
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
