#!/bin/bash

# Navigate to the main directory of the application
cd "$(dirname "$0")/.."

# Activate the virtual environment
source venv/bin/activate

# Run the learning function for each project in the projects folder
for project in data/projects/*; do
    if [ -d "$project" ]; then
        echo "Learning from project: $(basename "$project")"
        python main.py learn_from_code "$project"
    fi
done

# Deactivate the virtual environment
deactivate

echo "Learning process completed for all projects."