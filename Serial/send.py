import serial

usb = serial.Serial('COM3', 9600, timeout=None, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS)

command = b"hi\n"

usb.write(command)
