import os
import sys

def is_git_directory(path):
    return '.git' in path.split(os.sep)

def print_file_tree(directory, outfile, ignore_patterns):
    for root, dirs, files in os.walk(directory):
        # Skip if current dir should be ignored
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_patterns)]
        files = [f for f in files if not should_ignore(os.path.join(root, f), ignore_patterns)]
        
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level + 1)
        outfile.write(f"{indent}{os.path.basename(root)}/\n")
        subindent = ' ' * 4 * (level + 2)
        for f in files:
            outfile.write(f"{subindent}{f}\n")

def read_gitignore(directory):
    ignore_patterns = []
    try:
        with open(os.path.join(directory, '.gitignore'), 'r') as file:
            ignore_patterns = [line.strip() for line in file.readlines() if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print("No .gitignore file found.")
    return ignore_patterns

def should_ignore(path, ignore_patterns):
    # Check if the specific file 'poetry.lock' should be ignored
    if 'poetry.lock' in path or '.git' in path:
        return True
    # Check against other ignore patterns
    for pattern in ignore_patterns:
        if pattern in path:
            return True
    return False

# Modify the concatenate_files function to include the file tree printout
def concatenate_files(directory, output_file):
    ignore_patterns = read_gitignore(directory)
    with open(output_file, 'w') as outfile:
        # Print the file tree at the beginning, respecting the ignore patterns
        print_file_tree(directory, outfile, ignore_patterns)
        outfile.write("\n\n# Beginning of file contents\n\n")
        # Then write the rest of the file contents
        for root, dirs, files in os.walk(directory):
            # Skip the .git directory and anything within it
            if is_git_directory(root):
                dirs[:] = []
                continue

            # Filter out ignored directories
            dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_patterns)]
            for file in files:
                if should_ignore(file, ignore_patterns) or is_git_directory(file):
                    continue
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                    outfile.write(f"\n\n# File: {file_path}\n")
                    outfile.write(infile.read())

def calculate_estimated_tokens(output_file):
    with open(output_file, 'r') as file:
        content = file.read()
        # Each token is estimated to be about 4 characters long
        estimated_tokens = len(content) // 4
        return estimated_tokens

def main():
    repo_directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    output_file = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.getcwd(), "repo_dump.txt")
    concatenate_files(repo_directory, output_file)
    estimated_tokens = calculate_estimated_tokens(output_file)
    print(f"All files have been concatenated into {output_file}")
    print(f"Estimated token count: {estimated_tokens:,}")

if __name__ == "__main__":
    main()
