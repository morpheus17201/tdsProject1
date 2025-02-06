# A2. Format the contents of /data/format.md using prettier@3.4.2, updating the file in-place


import subprocess
import os


async def format_file_with_prettier(file_path, prettier_version="3.4.2"):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        return

    # Run the npx prettier command to format the file in-place
    subprocess.run(
        ["npx", "--yes", f"prettier@{prettier_version}", "--write", file_path],
        check=True,
    )
    print(f"Formatted {file_path} using Prettier version {prettier_version}.")


# Path to the file
file_path = "/data/format.md"

# Version of Prettier
prettier_version = "3.4.2"  # You can change this version as needed

# Call the function to format the file
if __name__ == "__main__":
    format_file_with_prettier(file_path, prettier_version)
