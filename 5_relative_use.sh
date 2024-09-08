#!/bin/bash
root=$(df / | awk 'NR==2 {print $2}')
home_usage=$(du -sk $HOME | awk '{print $1}')
percentage_used=$( echo "scale=2; ($home_usage / $root) * 100" | bc)
echo "Home directory usage is $percentage_used% of the root directory." 
