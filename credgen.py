#!/usr/bin/env python

import sys
import os
import columns

level='authPriv'
protocol='SHA'
privacy_protocol='DES'
user='snmpv3'
auth_passphrase='snmpv3.goesr'
privacy_passphrase='snmpv3.goesr'

if len(sys.argv) == 1:
    print "Need hostfile"
    print ','.join(columns.columns)
    sys.exit
else:
    for fname in sys.argv[1:]:
        if os.path.exists(fname):
            hostArray = []
            allHosts = open(fname, 'rt').readlines()
            title = ",".join(columns.columns)
            print title
            for h in allHosts:
                line=h.rstrip()+","+level+","+protocol+","+privacy_protocol+","+privacy_passphrase+","+user+","+auth_passphrase+","+h[7:10]
                print line
