import os
import json


async def extract_titles_from_markdown_files(input_folder, output_file_path):
    index = {}

    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.startswith("# "):
                            title = line[2:].strip()
                            relative_path = os.path.relpath(file_path, input_folder)
                            relative_path_with_slash = relative_path.replace("\\", "/")
                            index[relative_path_with_slash] = title
                            break

    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=4)


# Example usage
if __name__ == "__main__":
    input_directory = "/data/docs/"
    output_index_file = "/data/docs/index.json"
    extract_titles_from_markdown_files(input_directory, output_index_file)
