import serial
import re
import time
port = serial.Serial("COM5", baudrate=9600, timeout=10.0)
lamp = serial.Serial("COM3", baudrate=9600)

max=38.70
min=33.33

while True: 
    
    port.write('O2CRLF'.encode('ascii'))

    x = port.read(14)
    
    x=x.decode()
    chcek=x.split(" ")      #จะได้ค่าเป็นlist[+....(ค่าวัด),(หน่วย),SหรือU]
    print(chcek)
    
    if not chcek[2].startswith('S') :
        continue
        
    else:
        data = re.findall('[1-9]+[0-9]+.[0-9]+', chcek[0])
        if data == []:
            continue
        data_final = str(data[0])+chcek[1]
        data_chcek = float(data[0])

        if data_chcek >max or data_chcek<min:
            lamp.write('@??S100000!@??G!'.encode('ascii'))
            print('bad')
            
        else:
            lamp.write('@??S001000!@??G!'.encode('ascii'))
            print('good')

        
        print(data_final)


    
            

