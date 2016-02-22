#!/bin/bash

RED=1
GREEN=2
OFF=7

tput setaf $GREEN
echo OK
tput setaf $OFF

tput setaf $RED
echo FAIL
tput setaf $OFF


