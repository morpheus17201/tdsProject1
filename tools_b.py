tools_b = [
    {
        # B1
        # B2
        # B3
        # B4
        # B5
        # B6
        # B7
        # B8
        # B9
        {
            "type": "function",
            "function": {
                "name": "convert_markdown_to_html",
                "description": "Convert given markdown file to html. If the output file path is provided, the html will be written to the file. If output file path is not provided set it to empty string and return the converted html output as string",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "input_file_path": {
                            "type": "string",
                            "description": "Path where the input markdown file is stored.",
                        },
                        "output_file_path": {
                            "type": "string",
                            "description": "Path to the output file where the sorted contacts will be written. Set to empty string if the output is to be returned and not written as a file",
                        },
                    },
                    "required": ["input_file_path", "output_file_path"],
                    "additionalProperties": False,
                },
                "strict": True,
            },
        },
        # B10
    },
]
