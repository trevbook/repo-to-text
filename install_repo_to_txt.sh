#!/bin/bash

# Determine the directory where this script is located
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Modify repo_to_txt.sh to include the full path to repo_to_txt.py
# Check if we're on macOS and adjust the sed command accordingly
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS, which uses BSD sed
    sed -i '' "s|python repo_to_txt.py|python \"${SCRIPT_DIR}/repo_to_txt.py\"|g" "${SCRIPT_DIR}/repo_to_txt.sh"
else
    # Assume Linux, using GNU sed
    sed -i "s|python repo_to_txt.py|python \"${SCRIPT_DIR}/repo_to_txt.py\"|g" "${SCRIPT_DIR}/repo_to_txt.sh"
fi

# Define the alias command with the full path to the repo_to_txt.sh script
ALIAS_COMMAND="alias repo_to_text='${SCRIPT_DIR}/repo_to_txt.sh'"

# Check if the alias already exists in the .zshrc file
if grep -q "alias repo_to_text=" ~/.zshrc; then
    echo "Updating existing alias in .zshrc"
    # Replace the existing alias with the new one
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "/alias repo_to_text=/c\\
        $ALIAS_COMMAND
        " ~/.zshrc
    else
        sed -i "/alias repo_to_text=/c\\
        $ALIAS_COMMAND
        " ~/.zshrc
    fi
else
    echo "Adding new alias to .zshrc"
    # Append the new alias command to the end of the .zshrc file
    echo "$ALIAS_COMMAND" >> ~/.zshrc
fi

echo "Installation complete. You may need to restart your terminal or source ~/.zshrc"
