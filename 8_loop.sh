#!/bin/bash

threshold=90

for i in {1..100}
do
if
	[ $i -le $threshold ]
then
	echo $i
elif  
	[ $i -gt $threshold ]
then
	echo "$i is greater than threshold: $threshold"
fi
done