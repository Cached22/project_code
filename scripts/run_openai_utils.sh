#!/bin/bash

# Navigate to the main application directory
cd "$(dirname "$0")/.."

# Activate the virtual environment
source venv/bin/activate

# Run the OpenAI utilities
python -m openai_utils.generate_response

# Deactivate the virtual environment
deactivate

# Return to the original directory
cd -