import serial, time
s = serial.Serial('/dev/ttyACM0',9600)
time.sleep(1)
cmd = input("Kaskyta: ")
s.write(cmd.encode())


