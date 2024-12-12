#!/bin/bash

echo "Running tests..."

pytest tests

if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Tests failed! Check logs for details."
    exit 1
fi
