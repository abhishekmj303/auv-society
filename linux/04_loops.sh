#!/bin/bash

echo "Listing numbers from 1 to 10..."

echo
echo "With 'for' loop: (traversal)"
for i in {1..10}; do
    printf "$i "
done
printf "\n"

echo
echo "With 'for' loop: (C-style)"
for ((i=1; i<=10; i++)); do
    printf "$i "
done
printf "\n"

echo
echo "With 'while' loop: "
i=1
while [ $i -le 10 ]; do
    printf "$i "
    i=$((i+1))
done
printf "\n"

echo
echo "With 'until' loop: "
i=1
until [ $i -gt 10 ]; do
    printf "$i "
    i=$((i+1))
done
printf "\n"