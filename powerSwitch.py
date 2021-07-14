#!/usr/bin/env python
#updated 

import RPi.GPIO as GPIO
import subprocess


GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(3, GPIO.RISING)

subprocess.call(['shutdown', '-h', 'now'], shell=False)