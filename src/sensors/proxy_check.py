import RPi.GPIO as GPIO
import time

def proxy_check(inp):
    proxy_stat = GPIO.input(inp)
    print(f"Proximity Value is {proxy_stat}")
    return(proxy_stat)