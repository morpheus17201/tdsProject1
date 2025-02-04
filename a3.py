# A3. The file /data/dates.txt contains a list of dates, one per line.
# Count the number of Wednesdays in the list, and write just the number
# to /data/dates-wednesdays.txt

import os
from datetime import datetime

# Define the paths using os.path


def count_given_weekday_in_dates(
    day_of_week=r"wednesday",
    input_file_path=r"/data/dates.txt",
    output_file_path=r"/data/dates-wednesdays.txt",
):

    base_path = r"/data"
    input_file_path = os.path.join(base_path, "dates.txt")
    output_file_path = os.path.join(base_path, "dates-wednesdays.txt")

    # Check if input file exists
    if os.path.exists(input_file_path):
        # Open the file containing the dates
        with open(input_file_path, "r") as file:
            dates = file.readlines()

        # Initialize a counter for Wednesdays
        day_count = 0

        # Adjust weekday received to lowercase
        day_of_week_lowercase = day_of_week.lower().strip()

        # Loop through each date in the list
        for date_str in dates:
            # Remove any extra whitespace like newlines
            date_str = date_str.strip()

            # Try to parse the date
            try:
                date_obj = datetime.strptime(
                    date_str, "%Y-%m-%d"
                )  # Adjust format if needed
                # Check if it's a Wednesday (weekday() returns 2 for Wednesday)
                # if date_obj.weekday() == 2:
                if date_obj.strftime("%A").lower() == day_of_week_lowercase:
                    day_count += 1
            except ValueError:
                continue  # Skip invalid date formats

        # Write the count of Wednesdays to the output file
        with open(output_file_path, "w") as output_file:
            output_file.write(str(day_count))
    else:
        print(f"Error: The file {input_file_path} does not exist.")


# Call the function to format the file
if __name__ == "__main__":
    count_wednesdays_in_dates(
        input_file_path=r"/data/dates.txt",
        output_file_path=r"/data/dates-wednesdays.txt",
    )
