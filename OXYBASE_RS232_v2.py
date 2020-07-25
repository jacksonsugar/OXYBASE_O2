import time
import serial

reply = ''



ser= serial.Serial(
	port='/dev/ttyUSB0', #serial port the object should read
	baudrate= 19200,      #rate at which information is transfered over comm channel
	parity=serial.PARITY_NONE, #no parity checking
	stopbits=serial.STOPBITS_ONE, #pattern of bits to expect which indicates the end of a character
	bytesize=serial.EIGHTBITS, #number of data bits
	timeout=1
)

time.sleep(1)

while(1):

	comm = 1

	print('Welcome to the OXYBASE tester v0.2 \n')

	print('1. Print status report')
	print('2. Data request in mode 1')
	print('3. Set temperature compensation with interne NTC 22k sensor active.')
	print('4. Stores currently measured values (phase and temperature) as low pO 2 calibration')
	print('5. Stores currently measured values (phase and temperature) as high pO 2 calibration')
	print('6. Returns self-test message\n\n')
	print('0. Type your own command')

	func = raw_input('-')

	if func == '1':

		ser.write(b'repo\r')

		reply = ser.read_until('\r\r')

		print(reply)

	elif func == '2':

		ser.write(b'data\r')

		reply = ser.read_until('\r\r')

		print(reply)

	elif func == '3':

		ser.write(b'tmpa\r')

		reply = ser.read_until('\r\r')

		print(reply)

	elif func == '4':

		ser.write(b'calz\r')

		reply = ser.read_until('\r\r')

		print(reply)
		
	elif func == '5':

		ser.write(b'calh\r')

		reply = ser.read_until('\r\r')

		print(reply)

	elif func == '6':

		ser.write(b'post\r')

		reply = ser.read_until('\r\r')

		print(reply)


	elif func == '0':

		while(comm == 1):

			print('Please type your commands below or q to exit:')

			cmd = raw_input('-> ')

			if cmd == 'q':
				comm = 0

			else:

				cmd = cmd + '\r'

				ser.write(cmd)

				reply = ser.read_until('\r\r')

				reply = '\n' + reply

				print(reply)

	else:
		print('You broke it..')