from flask import Flask, render_template, url_for, request
import serial
import re
import time
import pyodbc
import datetime

conn = pyodbc.connect('driver=ODBC Driver 17 for SQL Server;server=DESKTOP-H45D3IV;database=measured_data;trusted_connection=yes;')
cursor = conn.cursor()
while 1 :
    try:
        cursor.execute("""
        CREATE TABLE Measured (
        value       FLOAT ,
        Tool        char(20),
        time        DATETIME2,
        go_nogo       VARCHAR (20),
    
                         ) """)
        conn.commit()

    except:
        break
    # cursor.execute("""SELECT * FROM measured_data.dbo.Measured """)
    # cursor.execute("""
    # INSERT INTO measured_data.dbo.Measured(value,Tool,time,gonogo) 
    # VALUES ( ?, ?,  CURRENT_TIMESTAMP)""", (2.5,' vernear-100',))
              
    # conn.commit()
tool = serial.Serial("COM4", 57600, timeout=10)
lamp = serial.Serial("COM3")

toolname_list=[]
go_list=[]
nogo_list=[]

limit_min = input('enter range min')
try:
    limit_min=float(limit_min)
    
except:
    print('plaese insert number')
limit_max = input('enter range max')
try:
    limit_max = float(limit_max)
  
except:
    print('plaese insert number')

while 1 :
    if limit_min > limit_max:
        print('ใส่ค่าmin max ให้ถูกต้อง')
        break

    if tool.inWaiting():
        read_byte=tool.read(tool.inWaiting())
            
        print(read_byte)
        k = read_byte.decode("utf-8")
        print(k)
        k = k.split('+')
        if len(k)==1: continue
        if not k[0].startswith('D'):
            print('error please try aging')
            continue
        print(type(k[0]))
        toolname=k[0]
        
             
        try :
            
            num = re.findall('[1-9]+.[0-9]+',k[1])
            value_list=[float(i) for i in num]
            
            
            if value_list[0]> 100:
                num = re.findall('[0]+.[0-9]+', k[1])
                value_list = [float(i) for i in num]
                
            print(value_list[0])

        
    
        except KeyboardInterrupt: break
        except:
            print('try aging')
            continue
        
           
        if value_list[0] >= limit_min and value_list[0] < limit_max:
            go_list.append(value_list[0])
            lamp.write('@??S001000!@??G!'.encode('ascii'))
            print('go')
            print('number go: ',len(go_list))
            cursor.execute("""SELECT * FROM measured_data.dbo.Measured """)
            cursor.execute("""
            INSERT INTO measured_data.dbo.Measured(value,Tool,time,go_nogo) 
            VALUES (?,?,CURRENT_TIMESTAMP,?)""", (value_list[0], toolname, 'pass'))

            conn.commit()
        else:
            nogo_list.append(value_list[0])
            lamp.write('@??S100000!@??G!'.encode('ascii'))
            print('no go')
            print('number nogo: ',len(nogo_list))
            cursor.execute("""SELECT * FROM measured_data.dbo.Measured """)
            cursor.execute("""
            INSERT INTO measured_data.dbo.Measured(value,Tool,time,go_nogo) 
            VALUES (?,?,CURRENT_TIMESTAMP,?)""", (value_list[0], toolname, 'fail'))

            conn.commit()

        time.sleep(0.5)
        lamp.write('@??S000000!@??G!'.encode('ascii'))
        


# if __name__=='__main__':
     #creat_table()



        



