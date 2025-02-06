import sqlite3


async def calculate_ticket_sales(input_file_path, output_file_path, ticket_type="Gold"):
    # Connect to the SQLite database
    conn = sqlite3.connect(input_file_path)
    cursor = conn.cursor()

    ticket_type = ticket_type.strip()

    # Query to get the total sales for the 'Gold' ticket type
    cursor.execute(
        # f"SELECT SUM(units * price) FROM tickets WHERE type like %'{ticket_type}'%"
        "SELECT SUM(units * price) FROM tickets WHERE type LIKE ?",
        ("%" + ticket_type + "%",),
    )
    total_sales = cursor.fetchone()[0]

    # If there are no Gold tickets, the result will be None, so we default to 0
    if total_sales is None:
        total_sales = 0.0

    # Write the result to the output file
    with open(output_file_path, "w") as output_file:
        output_file.write(f"{total_sales}")

    # Close the database connection
    conn.close()

    print(
        f"Total sales for Gold tickets = {total_sales} have been written to {output_file_path}"
    )


if __name__ == "__main__":
    input_file_path = "/data/ticket-sales.db"
    output_file_path = "/data/gold_ticket_sales.txt"
    calculate_ticket_sales(input_file_path, output_file_path)
