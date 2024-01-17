```sh
#!/bin/bash

# This script will install all the necessary dependencies for the application.

# Ensure the script is run with superuser privileges.
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Update package lists to ensure we get the latest versions.
apt-get update

# Install Python3 and Pip if they are not already installed.
apt-get install -y python3 python3-pip

# Navigate to the directory containing the requirements.txt file.
cd "$(dirname "$0")/.."

# Install the required Python libraries specified in requirements.txt.
pip3 install -r requirements.txt

# Verify the installation of the required libraries.
echo "Verifying the installation of the required Python libraries..."
pip3 freeze

echo "All dependencies have been installed successfully."
```