#!/bin/bash

# Navigate to the main directory of the application
cd "$(dirname "$0")/.."

# Define the directory containing the projects to enhance
PROJECTS_DIR="data/projects_metadata.json"

# Read the projects metadata to get the list of projects
PROJECTS=$(jq -r '.projects[] | .path' "$PROJECTS_DIR")

# Loop through each project path
for PROJECT_PATH in $PROJECTS; do
    # Check if the project directory exists
    if [ -d "$PROJECT_PATH" ]; then
        # Find all Python files in the project directory
        FILES=$(find "$PROJECT_PATH" -name '*.py')
        
        # Loop through each Python file
        for FILE in $FILES; do
            # Run the enhancement function and capture the output
            ENHANCED_CODE=$(python3 main.py enhance "$FILE")
            
            # Define the path for the enhanced code output
            ENHANCEMENT_OUTPUT_PATH="data/output/enhancements/$(basename "$FILE")"
            
            # Save the enhanced code to the output path
            echo "$ENHANCED_CODE" > "$ENHANCEMENT_OUTPUT_PATH"
            
            # Output the result
            echo "Enhanced code for $FILE has been saved to $ENHANCEMENT_OUTPUT_PATH"
        done
    else
        # Output an error message if the project directory does not exist
        echo "Error: Project directory $PROJECT_PATH does not exist."
    fi
done

# End of the enhancement script
