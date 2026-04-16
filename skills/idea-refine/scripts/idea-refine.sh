#!/bin/bash

# Initialize the ideas directory in the current workspace
IDEAS_DIR="./docs/ideas"

if [ ! -d "$IDEAS_DIR" ]; then
    echo "Creating ideas directory: $IDEAS_DIR"
    mkdir -p "$IDEAS_DIR"
    
    # Create a README.md in the ideas directory if it doesn't exist
    if [ ! -f "$IDEAS_DIR/README.md" ]; then
        echo "# Project Ideas" > "$IDEAS_DIR/README.md"
        echo "" >> "$IDEAS_DIR/README.md"
        echo "This directory contains refined ideas and one-pagers generated during ideation sessions." >> "$IDEAS_DIR/README.md"
    fi
    
    echo "Initialization complete."
else
    echo "Ideas directory already exists: $IDEAS_DIR"
fi
