#!/bin/bash
dna_seq="ACTGACGATCGACTGACGTACGTACGTA"

count_A=$(echo "$dna_seq" | grep -o "A" | wc -l)
count_C=$(echo "$dna_seq" | grep -o "C" | wc -l)
count_G=$(echo "$dna_seq" | grep -o "G" | wc -l)
count_T=$(echo "$dna_seq" | grep -o "T" | wc -l)
total_count=$((count_A+count_C+count_G+count_T))

echo "Total Nucleotide count: $total_count "
echo "Nucleotide counts: "
echo "A: $count_A"
echo "C: $count_C"
echo "G: $count_G"
echo "T: $count_T"
