import json


async def sort_contacts_file(
    input_file_path=r"/data/contacts.json",
    output_file_path=r"/data/contacts-sorted.json",
):
    # Read the data from the input file
    with open(input_file_path, "r") as infile:
        data = json.load(infile)

    # Sort the data by 'last_name' first, then by 'first_name'
    sorted_data = sorted(data, key=lambda x: (x["last_name"], x["first_name"]))

    # Write the sorted data to the output file
    with open(output_file_path, "w") as outfile:
        json.dump(sorted_data, outfile, indent=4)


if __name__ == "__main__":
    # Example usage
    input_path = r"/data/contacts.json"  # Replace with your input file path
    output_path = r"/data/contacts-sorted.json"  # Replace with your output file path

    sort_contacts_file(input_path, output_path)
