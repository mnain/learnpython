#!/usr/bin/python
#
# gentemplate.py
#

import sys
import math
import random
import getopt
import logging
import logging.config

class GenTemplate:
    # class vars
    digitList = "0123456789"
    upperList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerList = "abcdefghijklmnopqrstuvwxyz"
    punctList = "!@#^&*-_+="
    passLen   = 14
    freq = { }
    logger = None
    noPunct = False

    #
    # init method
    #
    def __init__(self, length=14, usePunct=False):
        self.passLen = length
        self.freq = { }
        logging.config.fileConfig('gentemplate.cfg')
        self.logger = logging.getLogger('gentemplate')
        self.noPunct = usePunct

    #
    # show method
    #
    def show(self):
        rc = "GenTemplate("
        rc = rc + str(self.passLen) + ", "
        rc = rc + self.digitList + ", "
        rc = rc + self.upperList + ", "
        rc = rc + self.lowerList + ", "
        rc = rc + self.punctList + ","
        rc = rc + str(self.noPunct) + ")"
        self.logger.info(rc)
        return rc

    #
    # generateTemplate method
    #
    def generateTemplate(self):
        self.clearFreq()
        tmpl = 'A'
        for i in range(self.passLen-1):
            ndx = random.randint(1,4)
            #print(ndx)
            if ndx == 1:
                tmpl = tmpl + '9'
                if 'digit' in self.freq.keys():
                    self.freq['digit'] = self.freq['digit'] + 1
                else:
                    self.freq['digit'] = 1
            # if 2 then upper
            if ndx == 2:
                tmpl = tmpl + 'A'
                if 'upper' in self.freq.keys():
                    self.freq['upper'] = self.freq['upper'] + 1
                else:
                    self.freq['upper'] = 1
            # if 3 then lower
            if ndx == 3:
                tmpl = tmpl + 'a'
                if 'lower' in self.freq.keys():
                    self.freq['lower'] = self.freq['lower'] + 1
                else:
                    self.freq['lower'] = 1
            # if 4 then punct
            if ndx == 4:
                if self.noPunct == False:
                    tmpl = tmpl + ','
                    if 'punct' in self.freq.keys():
                        self.freq['punct'] = self.freq['punct'] + 1
                    else:
                        self.freq['punct'] = 1
                else:
                    tmpl = tmpl + 'a'
                    if 'lower' in self.freq.keys():
                        self.freq['lower'] = self.freq['lower'] + 1
                    else:
                        self.freq['lower'] = 1
        self.logger.info(tmpl)
        return tmpl

    #
    # checkFreq - check that each template contains each type
    #
    def checkFreq(self):
        self.logger.info("checkFreq: "+str(self.freq)+ str(len(self.freq)))
        if self.noPunct and len(self.freq) == 3:
            self.logger.info("checkFreq: "+str(self.freq))
            return True
        if len(self.freq) == 4:
            self.logger.info("checkFreq: "+str(self.freq))
            return True
        return False

    #
    # handle CLI arguments passed
    #
    def handleArgs(self, argv):
        self.passLen = 14
        opts,args = getopt.getopt(sys.argv[1:], "l:p")
        for o,a in opts:
            if o == "-l": # length
                self.passLen = int(a)
                self.logger.info("passlen: "+str(self.passLen))
            if o == "-p": # no punctuation
                self.noPunct = True
                self.logger.info("noPunct: "+str(self.noPunct))

    #
    # get current set length
    #
    def getLength(self):
        self.logger.info("length: "+str(self.passLen))
        return self.passLen

    #
    # generate - invokes generateTemplate
    #
    def generate(self):
        tmpl = ''
        while 1:
            tmpl = self.generateTemplate()
            rc = self.checkFreq()
            self.logger.info(tmpl+" "+str(rc))
            if self.checkFreq():
                break
        self.logger.info("generate: "+tmpl)
        return tmpl

    #
    # clearFreq
    #
    def clearFreq(self):
        self.logger.info("clearFreq")
        self.freq = {}

if __name__ == "__main__":
    # print(sys.argv)
    gt = GenTemplate()
    gt.handleArgs(sys.argv[1:])
    # ss = gt.show()
    print(gt.generate())
