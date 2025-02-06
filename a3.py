# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "python-dateutil"
# ]
# ///


# A3. The file /data/dates.txt contains a list of dates, one per line.
# Count the number of Wednesdays in the list, and write just the number
# to /data/dates-wednesdays.txt

import os
from datetime import datetime
from dateutil import parser

# Define the paths using os.path


async def count_given_weekday_in_dates(
    day_of_week=r"wednesday",
    input_file_path=r"/data/dates.txt",
    output_file_path=r"/data/dates-wednesdays.txt",
):

    # base_path = r"/data"
    # input_file_path = os.path.join(base_path, "dates.txt")
    # output_file_path = os.path.join(base_path, "dates-wednesdays.txt")

    # Check if input file exists
    if os.path.exists(input_file_path):
        # Open the file containing the dates
        with open(input_file_path, "r") as file:
            dates = file.readlines()

        # Initialize a counter for Wednesdays
        day_count = 0

        # Adjust weekday received to lowercase
        day_of_week_lowercase = day_of_week.lower().strip()
        weekday_number = parser.parse(day_of_week_lowercase).weekday()

        # Loop through each date in the list
        for date_str in dates:
            # Remove any extra whitespace like newlines
            date_str = date_str.strip()

            # Try to parse the date
            try:
                date_obj = parser.parse(date_str)
                if date_obj.weekday() == weekday_number:
                    # if date_obj.strftime("%A").lower() == day_of_week_lowercase:
                    day_count += 1
            except parser.ParserError:
                print(f"Could not convert to date: {date_str}")
                continue  # Skip invalid date formats

        # Write the count of Wednesdays to the output file
        print(f"Number of {day_of_week}(s) found = {day_count}")
        with open(output_file_path, "w") as output_file:
            output_file.write(str(day_count))
    else:
        print(f"Error: The file {input_file_path} does not exist.")


# Call the function to format the file
if __name__ == "__main__":
    count_given_weekday_in_dates(
        day_of_week="mon",
        input_file_path=r"/data/dates.txt",
        output_file_path=r"/data/dates-wednesdays.txt",
    )
