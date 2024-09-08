#!/bin/bash
dir="/home/ibab/test"
output="empty_folders.txt"
find "$dir" -type d -empty | > "$output"
echo "List of empty subfolders is saved to $output."