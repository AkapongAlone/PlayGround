import subprocess
hwid = str(subprocess.check_output(
    'wmic bios get serialnumber ')).split('\\r\\n')[1].strip('\\r').strip()


check=len(hwid)
print(check)

def gen_key(hwid):
  serial=[]
  while len(hwid)<10:
          hwid=hwid+'S'
          return hwid
  if len(hwid)>8:
          print(hwid[:8])
          hwid=hwid[:8]
          return hwid
kuy=gen_key(hwid)  
print(kuy)