# LIFI-based-on-python-and-embedded-C



The following project demonstrates a working communication system that utilizes laser for communication.
serial python library is used 

On Transmitter side
1.Python script is used to send the image pixel values via serial to a microcontroller which then drives the laser diode as per the values obtained. 


on Reciever side
1.A microcontroller constantly listens on one of its serial port for changes in the LDR(light dependent resistance).
2.Once changes are recorded it transfers data via serial protocol.
3.Matlab is used to convert the data into image because it offers easy integration.
