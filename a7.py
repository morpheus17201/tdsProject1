import openai


def extract_sender_email(input_file_path, output_file_path):
    # Read the email content from the input file
    with open(input_file_path, "r") as file:
        email_content = file.read()

    # Define the prompt for the LLM
    prompt = f"Extract the sender's email address from the following email message:\n\n{email_content}\n\nSender's email address:"

    # Call the LLM to extract the sender's email address
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the email address from the response
    sender_email = response.choices[0].text.strip()

    # Write the email address to the output file
    with open(output_file_path, "w") as file:
        file.write(sender_email)


# Example usage
input_file_path = "/data/email.txt"
output_file_path = "/data/email-sender.txt"
extract_sender_email(input_file_path, output_file_path)
