import serial
import time
import numpy
import matplotlib as plt
from drawnow import *



ser=serial.Serial('/dev/ttyACM0',9600,timeout=0)
tauko = 1
pointer =[0,1,2,3,4]
sensor =[0,1,2,3,4]
temp = []
hum =[]
plt.ion()
laskuri= 0

def makeFig():
    #plt.ylim(-30,50)
    plt.xticks(numpy.arange(-30,50,1.0))
    plt.grid(True)
    plt.ylabel("Temp")
    plt.plot(temp,'ro-',label= "Celsiusta")
    plt.legend(loc= 'upper left')
    plt2 = plt.twinx()
    plt.ylim(0,100)
    plt2.plot(hum,"b^-",label="Ilmankosteus %")
    plt2.set_ylabel("Ilmankosteus %")
    plt2.ticklabel_format(useOffset= False)
    plt2.legend(loc = 'upper right')


while True:
    try:
        row= ser.readline()
        print(row)
        if(len(row)>3):
           sensor[0] = str(row[0:5])
           sensor[1] = str(row[5:10])
           sensor[0] = float(repr(sensor[0])[3:-2])
           sensor[1] = float(repr(sensor[1])[3:-2])
           print("Lampotila: ",sensor[1])
           print("Ilmankosteus: ",sensor[0])
           temp.append(sensor[1])
           hum.append(sensor[0])
           drawnow(makeFig)
           plt.pause(.000001)
           if(laskuri > 50):
               temp.pop(0)
               hum.pop(0)
    
    except IOError:
        print('Error tuli')
    time.sleep(tauko)
