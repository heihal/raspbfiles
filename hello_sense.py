'''
Tama on Raspberryn SenseHat palikan (emulaattorin) 
testailua
projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat
'''

from sense_emu import SenseHat
from random import randint
from time import sleep

def red():
	s.clear(255,0,0)
def blue():
	s.clear(0,0,255)
def green():
	s.clear(0,255,0)
def yellow():
	s.clear(255,255,0)


def testaa(temp,p,hum):
	if 18.3 < temp < 26.7:
		if 979 < p < 1027:
			if 57 < hum < 63:
				return True
			else:
				return False
		else:
			return False
	else:
		return False

s = SenseHat()

c = (0,255,244)
y= (255,255,0)
pun = (255,0,0)
vih = (0,255,0)
bg = y

x = 0

while x < 10:
	v = (randint(0,255),randint(0,255),randint(0,255))
	s.show_letter("H",text_colour = v, back_colour = bg)
	x+=1
	sleep(1)
	
s.clear()
p = s.get_pressure()
temp = s.get_temperature()
hum = s.get_humidity() 
print("Paine:(", p, " mbar")
print("Lampotila:", temp, "C")
print("Ilmankosteus:", hum, "%\n")

if testaa(temp, p, hum):
	bg = vih
else:
	bg = pun
s.show_message("Lampotila: {0} Paine: {1} Ilmankosteus {2}".format(temp,p,hum),back_colour = bg)
	
s.clear()

#Tata osuutta ei pysty testamaan emulaattorilla, nayttaa nollaa
'''
o = s.get_orientation()
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]
print("pitch {0} roll {1} yaw {2}".format(pitch, roll,yaw))

s.show_letter("J")
i = 0
while i < 10:
	acc = s.get_accelerometer_raw()
	x = acc['x']
	y = acc['y']
	z = acc['z']
	x,y,z = round(x,0),round(y,0),round(z,0)	
	print("x = {0},y = {1},z = {2}". format(x,y,z))
	if x == -1:
		s.set_rotation(180)
	elif y == 1: 
		s.set_rotation(90)
	elif y == -1:
		s.set_rotation(270)
	else:
		s.set_rotation(0)
		
	sleep(1)
	i +=1
'''
s.stick.direction_up = red
s.stick.direction_down = blue
s.stick.direction_left = green
s.stick.direction_right = yellow
s.stick.direction_middle = s.clear

while True:
	pass
