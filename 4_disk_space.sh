#!/bin/bash
threshold=70

disk_usage=$(df $HOME | awk 'NR==2 {print $5}'| sed s/%//)

if [ $disk_usage -ge $threshold ]
then
	echo "Warning: Current disk($disk_usage) usage has crossed the threshold($threshold) "
else
	echo "Current disk usage($disk_usage%) is under threshold($threshold%)"
fi