#!/usr/bin/python

import sys
import time
import datetime
import calendar

if __name__ == "__main__":
    argCount = len(sys.argv[1:])
    month = year = 0
    onlyMonth = True
    # print("argCount : "+str(argCount))
    try:
        if argCount == 0:
            # print("argCount==0")
            year = int(time.strftime('%Y'))
            month = int(time.strftime('%m'))
            onlyMonth = True
            if year < 1970 or year > 2037 or month < 1 or month > 12:
                sys.stderr.write("invalid month : %d %d\n" % (month,year))
                sys.exit(2)
        if argCount == 1:
            # print("argCount==1")
            year = int(sys.argv[1])
            onlyMonth = False
            # dt = datetime.datetime()
            # year = int(time.strftime('%Y'))
            if year < 1970 or year > 2037:
                sys.stderr.write('Invalid year %d' % year)
        if argCount == 2:
            # print("argCount==2")
            month = int(sys.argv[1])
            year = int(sys.argv[2])
            onlyMonth = True
            if year < 1970 or year > 2037 or month < 1 or month > 12:
                sys.stderr.write("invalid month : %d\n" % month)
                sys.exit(2)
        # sys.stdout.write("Month = %d, Year = %d\n" % (month,year))
        # generateCal(month, year)
        if onlyMonth == False:
            tc = calendar.TextCalendar(0)
            tc.pryear(year)
        if onlyMonth == True:
            tc = calendar.TextCalendar(0)
            tc.prmonth(year, month)
    except:
        sys.stderr.write("Unable to convert arguments " + str(sys.argv[1:]))
        sys.exit(1)
