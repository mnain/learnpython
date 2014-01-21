import signal
import os
import subprocess
import time

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

pauseTime = 60
signal.signal(signal.SIGALRM, alarm_handler)
signal.alarm(3)  # 3 seconds
try:
    print "Waiting",pauseTime,"from",time.strftime("%H:%M:%S")
    time.sleep(pauseTime)
    signal.alarm(0)  # reset the alarm
except Alarm:
    print "Now",time.strftime("%H:%M:%S")
