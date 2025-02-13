import os


# async def write_most_recent_log_first_lines(
#     input_folder=r"/data/logs/", output_file_path=r"/data/logs-recent.txt", num_files=10
# ):
async def write_most_recent_log_first_lines(
    input_folder, output_file_path, num_files=10
):

    # Get a list of all .log files in the input folder
    log_files = [f for f in os.listdir(input_folder) if f.endswith(".log")]

    # Get full paths to the log files
    log_files = [os.path.join(input_folder, f) for f in log_files]

    # Sort the log files by modification time, most recent first
    log_files.sort(key=lambda f: os.path.getmtime(f), reverse=True)

    # Take the first 10 most recent files
    recent_files = log_files[:num_files]

    # Open the output file for writing
    with open(output_file_path, "w") as outfile:
        for log_file in recent_files:
            # Read the first line of each log file
            with open(log_file, "r") as infile:
                first_line = infile.readline().strip()
                # Write the first line to the output file
                outfile.write(first_line + "\n")


# Example usage

if __name__ == "__main__":
    input_folder = r"/data/logs/"  # Replace with your input folder path
    output_file_path = r"/data/logs-recent.txt"  # Replace with your output file path
    write_most_recent_log_first_lines(input_folder, output_file_path)
