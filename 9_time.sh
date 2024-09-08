#!/bin/bash

current_time=$(date +%H)

if [ "$current_time" -ge 5 ] && [ "$current_time" -lt 12 ]; then
    echo "Good morning!.It is "$(date +%H:%M)" "
elif [ "$current_time" -ge 12 ] && [ "$current_time" -lt 18 ]; then
    echo "Good afternoon!.It is "$(date +%H:%M)" "
else
    echo "Good night!.It is "$(date +%H:%M)" "
fi
