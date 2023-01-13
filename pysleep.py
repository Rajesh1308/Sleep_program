import time
import os

#rundll32.exe powrprof.dll,SetSuspendState 0,1,0

while True:
    time.sleep(1800)
    os.system('rundll32.exe powrprof.dll,SetSuspendState sleep')

