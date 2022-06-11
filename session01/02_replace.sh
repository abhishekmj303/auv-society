#!/bin/bash

read -p "Enter the file path : " fpath

echo
echo "Before:"
cat $fpath
echo

if [[ -w "${fpath}" ]]; then
    sed -i "s/0xA0/0x50/g" "${fpath}"
    sed -i "s/0xFF/0x7F/g" "${fpath}"
    echo "The file (${fpath}) has been edited."
else
    echo "Not able to edit: ${fpath}"
fi

echo
echo "After:"
cat $fpath
echo