#!/bin/bash
set -e

mkdir -p test
touch test/test.sh
chmod 777 test/test.sh
echo "Created and made \"test/test.sh\" as readable, writable and executable"
echo "Contents of folder: "
tree -p

echo
rm -rf test
echo "Deleted the entire directory: test"
echo "Contents of folder: "
tree -p