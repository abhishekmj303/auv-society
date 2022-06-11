#!/bin/bash

read -p "Enter the file path: " fpath

if [ -f $fpath ]; then
    echo "${fpath} exists"
    if [ -w $fpath ]; then
        echo "You have permission to edit: ${fpath}"
    else
        echo "You do not have permission to edit: ${fpath}"
    fi
else
    echo "${fpath} does not exist"
fi
