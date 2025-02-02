# Function summaries

#A2 
# format_file_with_prettier(file_path:str, prettier_version='3.4.2')

#A3
#count_wednesdays_in_dates(input_file_path=r"/data/dates.txt", output_file_path=r"/data/dates-wednesdays.txt") 




tools = {

#A1





#A2
{
  "name": "format_file_with_prettier",
  "description": "Format a markdown file using Prettier and update it in place.",
  "parameters": {
    "type": "object",
    "properties": {
      "file_path": {
        "type": "string",
        "description": "The path to the markdown file that needs to be formatted."
      },
      "prettier_version": {
        "type": "string",
        "description": "The version of Prettier to use for formatting (default is 3.4.2).",
        "default": "3.4.2"
      }
    },
    "required": ["file_path"]
  },
  "function": "format_file_with_prettier"
},

#A4

{
  "name": "count_wednesdays_in_dates",
  "description": "Count the number of Wednesdays in a list of dates and write the count to a file.",
  "parameters": {
    "type": "object",
    "properties": {
      "input_file_path": {
        "type": "string",
        "description": "Path to the input file containing a list of dates, one per line.",
        "default": "/data/dates.txt"
      },
      "output_file_path": {
        "type": "string",
        "description": "Path to the output file where the number of Wednesdays will be written.",
        "default": "/data/dates-wednesdays.txt"
      }
    },
    "required": ["input_file_path", "output_file_path"]
  },
  "function": "count_wednesdays_in_dates"
},

#A5



#A6


#A7



#A8




#A9




#A10


        }
