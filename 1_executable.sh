#!/bin/bash 

for file in /
do
	if [[ -x $file ]];
	 then
		ls -l $file
	fi
done
