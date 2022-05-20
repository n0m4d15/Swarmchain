import smbus
from time import sleep         

#MPU6050 Registers and their Address
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47
Register_A = 0             
Register_B = 0x01          
Register_mode = 0x02         
X_axis_H = 0x03             
Z_axis_H = 0x05             
Y_axis_H = 0x07             
declination = -0.00669          
pi = 3.14159265359     


def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)
	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def Magnetometer_Init():
    #write to Configuration Register A
    bus.write_byte_data(Device_Address, Register_A, 0x70)
    #Write to Configuration Register B for gain
    bus.write_byte_data(Device_Address, Register_B, 0xa0)
    #Write to mode Register for selecting mode
    bus.write_byte_data(Device_Address, Register_mode, 0)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)
    #concatenate higher and lower value
    value = ((high << 8) | low)
    #to get signed value from mpu6050
    if(value > 32768):
		value = value - 65536
    return value

def imu_data(sda1, scl1):
	bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
	Device_Address = 0x68   # MPU6050 device address
	MPU_Init()
	print ("Reading Data of Gyroscope and Accelerometer")
	#Read Accelerometer raw value
	acc_x = read_raw_data(ACCEL_XOUT_H)
	acc_y = read_raw_data(ACCEL_YOUT_H)
	acc_z = read_raw_data(ACCEL_ZOUT_H)
	#Read Gyroscope raw value
	gyro_x = read_raw_data(GYRO_XOUT_H)
	gyro_y = read_raw_data(GYRO_YOUT_H)
	gyro_z = read_raw_data(GYRO_ZOUT_H)
	#Full scale range +/- 250 degree/C as per sensitivity scale factor
	Ax = acc_x/16384.0
	Ay = acc_y/16384.0
	Az = acc_z/16384.0
	Gx = gyro_x/131.0
	Gy = gyro_y/131.0
	Gz = gyro_z/131.0
	print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
	
	Magnetometer_Init()     # initialize HMC5883L magnetometer 
	print (" Reading Heading Angle")
	#Read Accelerometer raw value
	x = read_raw_data(X_axis_H)
	z = read_raw_data(Z_axis_H)
	y = read_raw_data(Y_axis_H)
	heading = math.atan2(y, x) + declination
	#Due to declination check for >360 degree
	if(heading > 2*pi):
		heading = heading - 2*pi
	#check for sign
	if(heading < 0):
		heading = heading + 2*pi
	#convert into angle
	heading_angle = int(heading * 180/pi)
	print ("Heading Angle = %d°" %heading_angle)
	
	return(Ax, Ay, Az, Gx, Gy, Gz, heading_angle



