#!/bin/bash

# Navigate to the main directory of the application
cd "$(dirname "$0")/.."

# Source the configuration settings
source config/settings.py

# Define the directory containing the projects to be reviewed
PROJECTS_DIR=$PROJECTS_FOLDER_PATH

# Check if the projects directory exists
if [ ! -d "$PROJECTS_DIR" ]; then
  echo "The projects directory does not exist: $PROJECTS_DIR"
  exit 1
fi

# Find all Python files in the projects directory and run the review_code function on each
find "$PROJECTS_DIR" -name '*.py' | while read -r file; do
  echo "Reviewing code in file: $file"
  
  # Run the review_code function from the review_code.py module and save the output to the reviews folder
  python -c "from review.review_code import review_code; review_code('$file')" > "$REVIEWS_FOLDER_PATH/$(basename "$file" .py)_review.txt"
  
  # Check if the review was successful
  if [ $? -eq 0 ]; then
    echo "Review completed for file: $file"
  else
    echo "Review failed for file: $file" >&2
    # Save the error message to the errors folder
    echo "Review failed for file: $file" > "$ERRORS_FOLDER_PATH/$(basename "$file" .py)_error.txt"
  fi
done

echo "Code review process completed."