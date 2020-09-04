#!/bin/bash

#Exception handling - making sure correct num of args provided
if [[ $# -lt 2 || $# -gt 2 ]]; then
	echo "Error: Incorrect number of arguments. Provide two files."
	exit 1
fi

inputFile = $1
masterFile = $2

paste $1 $2

exit 0
