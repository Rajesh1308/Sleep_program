import time
import os

#rundll32.exe powrprof.dll,SetSuspendState 0,1,0

#Reference
#https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rundll32
#https://learn.microsoft.com/en-us/windows/win32/api/powrprof/nf-powrprof-setsuspendstate

while True:
    time.sleep(1800)
    os.system('rundll32.exe powrprof.dll,SetSuspendState sleep')

