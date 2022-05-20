from RPi.GPIO import GPIO
import time

def metal_detect(inp):
    metal_stat = GPIO.input(inp)
    print(f"Metal Detection Status is {metal_stat}")
    return(metal_stat)