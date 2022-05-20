# This is the Sensors Main Code
# Written by N0M4D15 on 20th May 2022

#import gps_loc, imu, metal_detect, proxy_check
from time import sleep
import random
# from RPi.GPIO import GPIO

PROX_1 = 1
PROX_2 = 2
IMU_SDA = 3
IMU_SCL = 4
MET_DET = 5
GPS_LOC = 6

#proxy_1_stat = proxy_check.proxy_check(PROX_1)
#proxy_2_stat = proxy_check.proxy_check(PROX_2)
#metal_stat = metal_detect.metal_detect(MET_DET)
#lat,longi = gps_loc.get_loc(GPS_LOC)
#Ax, Ay, Az, Gx, Gy, Gz, heading_angle = imu.imu_data(IMU_SDA, IMU_SCL)
Ax = random.uniform(0.04,0.06)
Ay = random.uniform(0.04,0.06)
Az = random.uniform(0.04,0.06)
Gx = random.uniform(0.04,0.06)
Gy = random.uniform(0.04,0.06)
Gz = random.uniform(0.04,0.06)
heading_angle = random.randint(12,15)
nmeatime = 113721.00
while True:
    Ax = random.uniform(0.041,0.061)
    Ay = random.uniform(0.041,0.061)
    Az = random.uniform(0.851,0.97)
    Gx = random.uniform(0.291,0.351)
    Gy = random.uniform(0.099,0.115)
    Gz = random.uniform(0.038,0.076)
    heading_angle = random.randint(12,15)
    print("Proximity 1 Value is 0")
    print("Proximity 2 Value is 0")
    print("Metal Detection status is False")
    print(f"NMEA Time: {nmeatime}")
    nmeatime = nmeatime + 1.0
    print("NMEA Latitude: 12.9882 NMEA Longitude: 77.7119")
    print ("Reading Data of Gyroscope and Accelerometer")
    print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az)
    print ("Reading Heading Angle")
    print (f"Heading Angle = {heading_angle} degrees")
    sleep(1)