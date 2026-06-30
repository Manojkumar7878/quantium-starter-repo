#!/bin/bash

# Activate the virtual environment
source venv/Scripts/activate

# Run the test suite
python -m pytest

# Return the appropriate exit code
if [ $? -eq 0 ]; then
    exit 0
else
    exit 1
fi