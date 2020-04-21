import serial
arduino = serial.Serial('COM14', 9600, timeout=.1)

while True:
	data = arduino.read()#the last bit gets rid of the new-line chars
	if data:
		print(data)
		file1 = open("image1.txt", "a")
		file1.write(data.decode('utf-8'))
		file1.write(',')
		file1.close()
