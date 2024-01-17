```sh
#!/bin/bash

# Define the path to the projects folder and the output reports folder
PROJECTS_FOLDER_PATH="../data/projects_metadata.json"
REPORTS_FOLDER_PATH="../data/output/reports/"

# Function to check if the required directories exist
check_directories() {
  if [ ! -d "$PROJECTS_FOLDER_PATH" ]; then
    echo "Projects folder does not exist."
    exit 1
  fi

  if [ ! -d "$REPORTS_FOLDER_PATH" ]; then
    echo "Reports folder does not exist. Creating..."
    mkdir -p "$REPORTS_FOLDER_PATH"
  fi
}

# Function to run analysis on all projects
run_analysis() {
  # Iterate over each project in the projects folder
  for project in $(ls $PROJECTS_FOLDER_PATH); do
    echo "Analyzing project: $project"
    python main.py analyze "$PROJECTS_FOLDER_PATH/$project" > "$REPORTS_FOLDER_PATH/${project}_report.json"
    if [ $? -ne 0 ]; then
      echo "Analysis failed for project: $project"
    else
      echo "Analysis complete for project: $project"
    fi
  done
}

# Check if the directories exist
check_directories

# Run the analysis
run_analysis

echo "Analysis script execution completed."
```