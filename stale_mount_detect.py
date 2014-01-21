import signal
import os
import subprocess
import time

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

def countLines(block):
    return block.count('\n')

global nfsMountPath
nfsMountPath = "/cygdrive/f"

if __name__ == "__main__":
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(3)  # 3 seconds
    try:
        print "Checking",nfsMountPath
        soutName = '/tmp/stdout.txt'
        serrName = '/tmp/stderr.txt'
        #sout = open(soutName, 'wt')
        #serr = open(serrName, 'wt')
        #rc = subprocess.Popen(['stat',nfsMountPath],shell=True, stdin=None, stdout=sout, stderr=serr).wait()
        cmd = ['stat', '-f', nfsMountPath]
        rc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
        signal.alarm(0)  # reset the alarm
        #print rc
        print countLines(rc)
    except Alarm:
        print "oops",nfsMountPath,"not accessible or stale mount"
