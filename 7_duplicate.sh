#!/bin/bash

input="input.txt"
output="output.txt"

sort $input | uniq > $output
cat $output