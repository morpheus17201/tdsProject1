# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx"
# ]
# ///


import httpx


from base_logger import logger
from common import OPENAI_API_URL, OPENAI_API_KEY
import json


async def extract_sender_email(input_file_path, output_file_path):
    # AIPROXY_TOKEN = os.environ["AIPROXY_TOKEN"]
    # Read the email content from the input file
    with open(input_file_path, "r") as file:
        email_content = file.read()

    # Define the prompt for the LLM
    # prompt = f"Extract the sender's email address from the following email message:\n\n{email_content}\n\nSender's email address:"
    model = "gpt-4o-mini"

    # Call the LLM to extract the sender's email address
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                # response = httpx.post(
                OPENAI_API_URL + r"chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "messages": [
                        {
                            "role": "system",
                            "content": "Extract the sender's e-mail address from the following email message",
                        },
                        {"role": "user", "content": f"{email_content}"},
                    ],
                },
            )

    except Exception as e:
        print(f"Error occurred while fetching response from GPT: {e}")
        raise e
        return

    result = response.json()
    print(f"Response received from GPT: {json.dumps(result, indent=2)}")
    sender_email = result["choices"][0]["message"]["content"]

    print(f"Sender's email id detected: {sender_email}")

    # Write the email address to the output file
    with open(output_file_path, "w") as file:
        file.write(sender_email)


# Example usage
if __name__ == "__main__":
    input_file_path = "/data/email.txt"
    output_file_path = "/data/email-sender.txt"
    extract_sender_email(input_file_path, output_file_path)
