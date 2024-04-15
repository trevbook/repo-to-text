# Repository to Text Dump Utility

This utility allows you to concatenate all the relevant files from a GitHub / GitLab repository into a single text file, ignoring files and directories as specified in `.gitignore` and other configurable settings. This can be helpful for dumping a repo into the context window of an LLM! 

## Features

- **Reads `.gitignore`**: Automatically ignores files and directories specified in the repository's `.gitignore`.
- **Filters Unnecessary Files**: Skips over files like Python bytecode (`.pyc`) and virtual environment directories.
- **Concatenates to a Single File**: Outputs the content of the repository into a single text file, with clear demarcations for the origin of each part.
- **Customizable Output Location**: Allows the user to specify the output file's location.

## Installation

1. Clone this repository or download the scripts to your local machine.
2. Ensure the scripts are in the same directory.
3. Make the scripts executable:
   ```bash
   chmod +x repo_to_txt.sh
   chmod +x install_repo_to_txt.sh
4. Run the `install_repo_to_txt.sh` script to modify your `~/.zshrc` file. This adds an alias to the `repo_to_text` command. 

## Usage

**BASIC USAGE:** Navigate to the root directory of your repo in a Terminal. Run `repo_to_text` to process the current repo and create a text file called `repo_dump.txt`. 

**ADVANCED USAGE:** To specify a different output file name and/or location, provide the desired path as an argument:

```
repo_to_text /path/to/your/repo /path/to/output/file.txt
```