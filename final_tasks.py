#!/usr/bin/python

#TODO: Modify SNMP Regex to match resonse for sysObjectId query
#TODO: Instead of outputting to syslog, output to a file in a format that is easily readable

import re
import subprocess
import syslog
import threading
import time

#Regular Expression Objects
regex_ping = re.compile(r".*(\d) received.*")
regex_snmp = re.compile(r"^SNMP*")
regex_isip = re.compile(r"^([\d]*\.[\d]*\.[\d]*\.[\d]*):(.*)")

#Variable to display debug output (False=Don't Display, True=Display)
debug = False

#PingStatus class used for multi-threaded ping sweep
class PingStatus(threading.Thread):
    def __init__ (self, ip, host):
        threading.Thread.__init__(self)
        self.ip = ip
        self.host = host
        self.status = 0

    def run(self):
        ping_comm = subprocess.Popen(['ping', '-q', '-c5', '-w10' , self.ip], stdout=subprocess.PIPE)
        for p_output_line in iter(ping_comm.stdout.readline,''):
            if(debug):
                print self.ip + " p_output_line: " + p_output_line
            if not p_output_line: break

            p_matches = re.match(regex_ping, p_output_line)
            if p_matches:
                self.status = int(p_matches.group(1))

#SnmpStatus class used for multi-threaded SNMP walk of F5 Virtual Servers
class SnmpStatus(threading.Thread):
    def __init__ (self, ip, host):
        threading.Thread.__init__(self)
        self.ip = ip
        self.host = host
        self.status = 0

    def run(self):
        #Note: this command assumes that F5-BIGIP-LOCAL-MIB has been loaded into MIB database for net-snmp-utils
        #snmp_comm = os.popen("snmpwalk -v3 -u ITNM -l authPriv -a SHA -a goesr_community3 -x AES128 -X goesr_community3p " + self.ip + " F5-BIGIP-LOCAL-MIB::ltmVsStatusAvailState", "r")
        #snmp_comm = subprocess.Popen(['snmpwalk', '-v3', '-r1', '-u', 'snmpv3', '-l', 'authPriv', '-a', 'SHA', '-A', 'snmpv3.goesr', '-x', 'DES', '-X', 'snmpv3.goesr', self.ip, 'sysObjectId'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        snmp_comm = subprocess.Popen(['snmpwalk', '-v3', '-r1', '-u', 'ITNM', '-l', 'authPriv', '-a', 'SHA', '-A', 'goesr_community3', '-x', 'AES128', '-X', 'goesr_community3p', self.ip, 'sysObjectId'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #snmp_comm = subprocess.Popen(['snmpwalk', '-v3', '-r1', '-u', 'solaceTraps', '-l', 'authPriv', '-a', 'MD5', '-A', 'solaceTraps1', '-x', 'DES', '-X', 'solaceTraps1', self.ip, 'sysObjectId'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
        for s_output_line in iter(snmp_comm.stdout.readline,''):
            if(debug):
                print "s_output_line: " + s_output_line
            if not s_output_line: break

            #Check to see if output matches expected format
            s_string_check = re.match(regex_snmp, s_output_line)
            if(debug):
                print "s_string_check: " + str(s_string_check)
            if s_string_check:
                self.status = 1

        for s_error_line in iter(snmp_comm.stderr.readline,''):
            if(debug):
                print "s_error_line: " + s_error_line

def loop():
    #Call loop() every 9 seconds
    #threading.Timer(9.0, loop).start()
	
    #Beginning of loop timestamp
    print "Begin loop " + time.ctime()

    #Initialize data structures
    ping_list = []
    snmp_list = []
    p_statusdict = {}
    s_statusdict = {}
    outfiledict = {}
    p_ipmatch = 0
    s_ipmatch = 0
    report = ["No response","One Response","Two Responses","Three Responses","Four Responses","Five Responses"]

    #Open file of IPs to read for ping sweep
    p_f = open('./SSD_Management_11_8_sorted.txt', 'r')

    #Iterate through list of IPs and create a PingStatus Thread for each ping command
    for p_ip in p_f:
        p_ipmatch = re.match(regex_isip, p_ip)	
        if p_ipmatch:
            #print p_ipmatch.group(1)
            #if p_ip:
            p_current_obj = PingStatus(p_ipmatch.group(1), p_ipmatch.group(2))
            ping_list.append(p_current_obj)
            p_current_obj.start()

    #Close file
    p_f.close()

    ping_failure_list = open('./ping_failures.txt', 'w')
    ping_success_list = open('./ping_success.txt', 'w')
    #Iterate through each Thread to determine status of host
    for pl_obj in ping_list:
        pl_obj.join()
		
        #Add current Thread status to p_statusdict dictionary data structure, with IP as key and status as value
        p_statusdict[pl_obj.host] = pl_obj.status
        if(debug):
            print "Status from " + pl_obj.host + " is " + report[pl_obj.status]
        if(pl_obj.status < 4):
            ping_failure_list.write(pl_obj.ip + ':' + pl_obj.host + '\n')
        else:
            ping_success_list.write(pl_obj.ip + ' ' + pl_obj.host + '\n')

    ping_failure_list.close()
    ping_success_list.close()
    
    #SNMP
    s_f = open('./SSD_Management_11_8_sorted.txt', 'r')

    for s_ip in s_f:
        s_ipmatch = re.match(regex_isip, s_ip)
        if s_ipmatch:
            if(debug):
                print s_ipmatch.group(1)
            s_current_obj = SnmpStatus(s_ipmatch.group(1), s_ipmatch.group(2))
            snmp_list.append(s_current_obj)
            s_current_obj.start()
    #Close snmp file
    s_f.close()

    snmp_failure_list = open('./snmp_failures.txt', 'w')
    snmp_success_list = open('./snmp_success.txt', 'w')

	
    #Iterate through each Thread to determine status of host
    for sl_obj in snmp_list:
        sl_obj.join()

        if(sl_obj.status == 1):
            snmp_success_list.write(sl_obj.ip + ' ' + sl_obj.host + '\n')
        else:
            snmp_failure_list.write(sl_obj.ip + ':' + sl_obj.host + '\n')

    snmp_failure_list.close()
    snmp_success_list.close()

    #Ending of loop timestamp
    print "End loop " + time.ctime()
	
if __name__ == "__main__":
    loop()
