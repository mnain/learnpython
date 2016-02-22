#!/bin/bash

if [ $# -eq 0 ]; then
	echo Need arguments
	exit 1
fi
FAIL=1
OK=2
OFF=7


for i in `cat $1`; do
	#echo $i
    prc=`ping -c 1 $i`
	j=`echo $prc | grep "1 received" | wc -l`
	#echo $j
	if [ $j -eq 1 ]; then
		tput setaf $OK
		echo $i OK
		tput setaf $OFF
	else
		tput setaf $FAIL
		echo $i FAIL
		tput setaf $OFF
	fi
done;

