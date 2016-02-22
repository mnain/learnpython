#!/bin/bash

#echo $1
for i in `cat $1`; 
do
	echo `nslookup $i`
done
