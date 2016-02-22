#!/usr/bin/env python

import sys
import os
import csv
from columns import *

level='authPriv'
protocol='SHA'
privacy_protocol='DES'
user='snmpv3'
auth_passphrase='snmpv3.goesr'
privacy_passphrase='snmpv3.goesr'

if len(sys.argv) == 1:
    print "Need hostfile"
    sys.exit
else:
    fname = sys.argv[1]
    if os.path.exists(fname):
        csvfile = open(fname, 'rb')
        csvreader = csv.DictReader(csvfile, columns)
        for row in csvreader:
            print row
