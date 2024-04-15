#!/bin/bash

# Default file name
OUTPUT_FILE="repo_text_dump.txt"

# Check if an output path is provided
if [ "$#" -eq 2 ]; then
    OUTPUT_FILE=$2
fi

# Call the Python script with the repository path and output file
python "/Users/thubbard/Documents/tools/mini-commands/repo-to-text/repo_to_txt.py"
