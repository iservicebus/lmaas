#!/bin/bash

# Get the path to the test file as a parameter
test_file_path="$1"

# Check if the parameter is provided
if [ -z "$test_file_path" ]; then
    echo "Error: Missing test file path as a parameter such as './run_test.sh ./src/data_models/chat/test_text.py'  "
    exit 1
fi

# Run the Python unittest command with the provided path
python3 -m unittest "$test_file_path"
