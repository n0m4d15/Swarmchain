# This is the Sensors Main Code
# Written by N0M4D15 on 20th May 2022

import gps_loc, imu, metal_detect, proxy_check
import time
from RPi.GPIO import GPIO

PROX_1 = 1
PROX_2 = 2
IMU_SDA = 3
IMU_SCL = 4
MET_DET = 5
GPS_LOC = 6

proxy_1_stat = proxy_check.proxy_check(PROX_1)
proxy_2_stat = proxy_check.proxy_check(PROX_2)
metal_stat = metal_detect.metal_detect(MET_DET)
lat,longi = gps_loc.get_loc(GPS_LOC)
Ax, Ay, Az, Gx, Gy, Gz = imu.imu_data(IMU_SDA, IMU_SCL)