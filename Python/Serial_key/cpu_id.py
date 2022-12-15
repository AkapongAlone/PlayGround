import subprocess

hwid = str(subprocess.check_output(
    'wmic bios get serialnumber ')).split('\\r\\n')[1].strip('\\r').strip()

print(hwid)

def gen_key(hwid):
  serial=[]
  for i in hwid:
    if i == 'A':
      serial.append('S')
      serial.append('8')
    elif i =='B':
      serial.append('E')
      serial.append('S')
    elif i =='C':
      serial.append('Q')
      serial.append('D')
    elif i =='D':
      serial.append('1')
      serial.append('L')
    elif i =='E':
      serial.append('8')
      serial.append('W')
    elif i =='F':
      serial.append('P')
      serial.append('K')
    elif i =='G':
      serial.append('J')
      serial.append('3')
    elif i =='H':
      serial.append('Q')
      serial.append('T')
    elif i =='I':
      serial.append('3')
      serial.append('R')
    elif i =='J':
      serial.append('U')
      serial.append('9')
    elif i =='K':
      serial.append('T')
      serial.append('E')
    elif i =='L':
      serial.append('M')
      serial.append('H')
    elif i =='M':
      serial.append('N')
      serial.append('C')
    elif i =='N':
      serial.append('R')
      serial.append('X')
    elif i =='O':
      serial.append('4')
      serial.append('B')
    elif i =='P':
      serial.append('Z')
      serial.append('A')
    elif i =='Q':
      serial.append('V')
      serial.append('M')
    elif i =='R':
      serial.append('Y')
      serial.append('N')
    elif i =='S':
      serial.append('T')
      serial.append('3')
    elif i =='T':
      serial.append('X')
      serial.append('A')
    elif i =='U':
      serial.append('W')
    elif i =='V':
      serial.append('5')
      serial.append('Y')
    elif i =='W':
      serial.append('H')
      serial.append('R')
    elif i =='X':
      serial.append('0')
      serial.append('S')
    elif i =='Y':
      serial.append('G')
      serial.append('0')
    elif i =='Z':
      serial.append('C')
      serial.append('B')
    elif i =='0':
      serial.append('A')
      serial.append('U')
    elif i =='1':
      serial.append('F')
      serial.append('5')
    elif i =='2':
      serial.append('I')
      serial.append('Q')
    elif i =='3':
      serial.append('L')
      serial.append('Y')
    elif i =='4':
      serial.append('D')
      serial.append('V')
    elif i =='5':
      serial.append('2')
      serial.append('S')
    elif i =='6':
      serial.append('6')
      serial.append('R')
    elif i =='7':
      serial.append('9')
      serial.append('H')
    elif i =='8':
      serial.append('7')
      serial.append('B')
    elif i =='9':
      serial.append('E')
      serial.append('J')
  serial_key=serial[0]+serial[1]+serial[2]+serial[3]+"-"+serial[4]+serial[5]+serial[6]+serial[7]+"-"+serial[8]+serial[9]+serial[10]+serial[11]+"-"+serial[12]+serial[13]+serial[14]+serial[15]
  return(serial_key)  

key_id=gen_key(hwid)

f = open("demofile2.txt", "a")
f.write(gen_key(hwid))
f.close()

# #open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())



try :
  f = open("demofile2.txt", "r")
  key_check=f.read()
  if key_check == key_id:
    #รันlogingเลย
  else:
    #รันหน้าwelcome
except:
  #รันหน้าwelcome