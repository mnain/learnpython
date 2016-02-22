#!/usr/bin/env python

import os
import sys
import csv
from columns import *
import config

credentialList = [ ]
cols = [
    columns[USERNAME],
    columns[AUTH_PROTOCOL],
    columns[AUTH_PASSPHRASE],
    columns[PRIVACY_PROTOCOL],
    columns[PRIVACY_PASSPHRASE],
]


def getCredList(fname):
    fh = open(fname, 'rt')
    csvReader = csv.DictReader(fh, cols)
    for row in csvReader:
        rowKeys = row.keys()
        for c in columns:
            if c not in rowKeys:
                if c == columns[LEVEL]:
                    row[c] = 'authPriv'
                else:
                    row[c] = None
        #print row
        credentialList.append(row)
    fh.close()
    print credentialList
    return credentialList

if __name__ == "__main__":
        getCredList('credentials.csv')
