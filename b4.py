# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "python-dateutil",
# ]
# ///


import subprocess
import os
import datetime


async def clone_and_commit(repo_url, clone_dir="", commit_message=""):
    """
    Clones a git repository, optionally modifies a file, and commits the changes.

    :param repo_url: URL of the git repository to clone.
    :param clone_dir: Directory where the repository will be cloned.
    :param commit_message: The message to use for the commit.
    :param file_to_edit: (Optional) Path of a file in the repo to modify.
    :param file_content: (Optional) New content to write to the file to edit.
    """
    try:
        #
        if clone_dir == "":
            NOW = datetime.now()
            clone_dir = os.path.join(
                [
                    "/",
                    "data",
                    "gitrepo",
                    datetime.datetime.strftime(
                        datetime.now(),
                    ),
                ]
            )

        # Clone the repository
        print(f"Cloning repository from {repo_url}...")
        subprocess.run(["git", "clone", repo_url, clone_dir], check=True)
        subprocess.run(["cd", clone_dir])

        # If a file is specified to be edited, update its content
        if file_to_edit and file_content:
            file_path = os.path.join(clone_dir, file_to_edit)
            print(f"Editing file {file_path}...")
            with open(file_path, "w") as file:
                file.write(file_content)

            # Add the file to the staging area
            subprocess.run(["git", "-C", clone_dir, "add", file_to_edit], check=True)

        # Commit the changes
        if commit_message == "":
            commit_message = "Sample commit message"
        print(f"Committing changes with message: {commit_message}")
        subprocess.run(
            ["git", "-C", clone_dir, "commit", "-m", commit_message], check=True
        )

        # Push the changes (optional)
        # subprocess.run(["git", "-C", clone_dir, "push"], check=True)

        print("Changes committed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during Git operation: {str(e)}")


# Example usage:
# clone_and_commit(
#     repo_url="https://github.com/yourusername/yourrepo.git",
#     clone_dir="/path/to/clone/directory",
#     commit_message="Added a new feature",
#     file_to_edit="example.py",
#     file_content="print('Hello World!')"
# )
