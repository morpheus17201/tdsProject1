# Function summaries

# A2
# format_file_with_prettier(file_path:str, prettier_version='3.4.2')

# A3
# count_wednesdays_in_dates(input_file_path=r"/data/dates.txt", output_file_path=r"/data/dates-wednesdays.txt")


tools = [
    # A1
    # A2
    {
        "type": "function",
        "function": {
            "name": "format_file_with_prettier",
            "description": "Format a markdown file using Prettier and update it in place.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The path to the markdown file that needs to be formatted.",
                    },
                    "prettier_version": {
                        "type": "string",
                        "description": "The version of Prettier to use for formatting (default is 3.4.2).",
                        # "default": "3.4.2",
                    },
                },
                "required": ["file_path", "prettier_version"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A3
    {
        "type": "function",
        "function": {
            "name": "count_given_weekday_in_date",
            "description": "Count the number of Wednesdays in a list of dates and write the count to a file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day_of_week": {
                        "type": "string",
                        "description": "Day of week to be counted, e.g. wednesday",
                    },
                    "input_file_path": {
                        "type": "string",
                        "description": "Path to the input file containing a list of dates, one per line.",
                        # "default": "/data/dates.txt",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the number of Wednesdays will be written.",
                        # "default": "/data/dates-wednesdays.txt",
                    },
                },
                "required": ["day_of_week", "input_file_path", "output_file_path"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A4
    {
        "type": "function",
        "function": {
            "name": "sort_contacts_file",
            "description": "Sort the contacts in the json input file by last_name then by first_name and write to given output file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_file_path": {
                        "type": "string",
                        "description": "Path to the input file containing the contacts to be sorted",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the sorted contacts will be written.",
                        # "default": "/data/dates-wednesdays.txt",
                    },
                },
                "required": ["input_file_path", "output_file_path"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A5
    {
        "type": "function",
        "function": {
            "name": "write_most_recent_log_first_lines",
            "description": "Write the first line of n most recent log files in input folder to output path.",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_folder": {
                        "type": "string",
                        "description": "Path to the input folder containing the log file to be processed",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the extracted contents of the log file  will be written.",
                        # "default": "/data/dates-wednesdays.txt",
                    },
                    "num_files": {
                        "type": "integer",
                        "description": "Number of most recent log files from which the content will be processed",
                        # "default": "/data/dates-wednesdays.txt",
                    },
                },
                "required": ["input_folder", "output_path", "num_files"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A6
    {
        "type": "function",
        "function": {
            "name": "extract_titles_from_markdown_files",
            "description": "Recursively traverse folder and extract first H1 title from each markdown file and write to output file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_folder": {
                        "type": "string",
                        "description": "Path to the input folder containing the markdown files to be processed",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the extracted contents of the markdown files will be written.",
                    },
                },
                "required": ["input_folder", "output_file_path"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A7
    {
        "type": "function",
        "function": {
            "name": "extract_sender_email",
            "description": "Extract sender's email from the given email message by passing it to the LLM model and write it to the given output file",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_file_path": {
                        "type": "string",
                        "description": "Path to the input file containing email message",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the extracted sender's email ID will be written",
                    },
                },
                "required": ["input_file_path", "output_file_path"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A8
    # A9
    # A10
]
