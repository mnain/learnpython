#!/usr/bin/python
#
# genpasswd.py
#

import sys
import math
import random
import getopt
import logging
import logging.config
import gentemplate

class GenPasswd:
    # class vars
    digitList = "0123456789"
    upperList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerList = "abcdefghijklmnopqrstuvwxyz"
    punctList = "-="
    passLen   = 14
    freq = { }
    logger = None
    noPunct = False
    template = None
    useTemplate = False

    #
    # init method
    #
    def __init__(self, length=14):
        self.passLen = length
        self.freq = { }
        logging.config.fileConfig('genpasswd.cfg')
        self.logger = logging.getLogger('genpasswd')

    #
    # show method
    #
    def show(self):
        rc = "GenPasswd("
        rc = rc + str(self.passLen) + ", "
        rc = rc + self.digitList + ", "
        rc = rc + self.upperList + ", "
        rc = rc + self.lowerList + ", "
        rc = rc + self.punctList + ","
        rc = rc + str(self.noPunct) + ")"
        self.logger.info(rc)
        return rc

    #
    # handle CLI arguments passed
    #
    def handleArgs(self, argv):
        self.passLen = 14
        opts,args = getopt.getopt(sys.argv[1:], "l:pt:")
        for o,a in opts:
            if o == "-l": # length
                self.passLen = int(a)
                self.logger.info("passlen: "+str(self.passLen))
            if o == "-p": # no punctuation
                self.noPunct = True
                self.logger.info("noPunct: "+str(self.noPunct))
            if o == "-t": # template
                self.template = a
                self.useTemplate = True

    #
    # get current set length
    #
    def getLength(self):
        self.logger.info("length: "+str(self.passLen))
        return self.passLen
        
    #
    # set length
    #
    def setLength(self, newLength):
        self.passLen = newLength

    #
    # getNoPunct
    #
    def getNoPunct(self):
        return self.noPunct

    #
    # setNoPunct
    #
    def setNoPunct(self, newValue):
        self.noPunct = newValue

    #
    # generate - invokes generateTemplate
    #
    def generate(self):
        self.logger.info('generate: ')
        newPasswd = self.genpass()
        return newPasswd
        
    #
    # genpass - generate password
    #
    def genpass(self):
        newPasswd = ''
        self.logger.info('genpass passwd len : '+str(self.getLength()))
        if self.useTemplate == False:            
            gentmpl = gentemplate.GenTemplate(self.getLength(),self.getNoPunct())
            tmplate = gentmpl.generateTemplate()
        else:
            tmplate = self.template
        # print('template: '+tmplate)
        self.logger.info('genpass : template : '+tmplate)
        prevEscape = False
        for indx in range(len(tmplate)):
            ch = tmplate[indx]
            if '\\' == ch:
                prevEscape = True
            if 'A' == ch: # upper
                v = self.upperList[random.randint(0,len(self.upperList)-1)]
                newPasswd = newPasswd + v
            elif 'a' == ch: # lower
                v = self.lowerList[random.randint(0,len(self.lowerList)-1)]
                newPasswd = newPasswd + v
            elif '9' == ch: # digit
                v = self.digitList[random.randint(0,len(self.digitList)-1)]
                newPasswd = newPasswd + v
            elif ',' == ch: # punct
                v = self.punctList[random.randint(0,len(self.punctList)-1)]
                newPasswd = newPasswd + v
            else: # anything else
                newPasswd = newPasswd + ch
        # print('Passwd: '+newPasswd)
        self.logger.info('newpasswd : '+newPasswd)
        return newPasswd

if __name__ == "__main__":
    # print(sys.argv)
    gp = GenPasswd()
    gp.handleArgs(sys.argv[1:])
    ss = gp.show()
    print(gp.generate())
