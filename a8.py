# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
# ]
# ///


import base64
import httpx
import os
import re


def extract_credit_card_number_from_text(text):
    # Regular expression pattern for credit card number (with or without spaces)
    card_number_pattern = r"\b(?:\d[ -]*?){13,19}\b"

    # Search for the card number in the given text
    match = re.search(card_number_pattern, text)

    if match:
        # Clean the card number (remove any spaces or hyphens)
        card_number = match.group(0).replace(" ", "").replace("-", "")
        return card_number
    else:
        return None


async def extract_numbers_from_image(input_file_path, output_file_path):
    # Read the image file and encode it in base64
    with open(input_file_path, "rb") as f:
        binary_data = f.read()
        image_b64 = base64.b64encode(binary_data).decode()

    # Data URI example (embed images in HTML/CSS)
    data_uri = f"data:image/png;base64,{image_b64}"

    OPENAI_API_KEY = os.environ["AIPROXY_TOKEN"]
    OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"

    try:
        async with httpx.AsyncClient() as client:
            # response = httpx.post(
            response = await client.post(
                OPENAI_API_URL,
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
                json={
                    "model": "gpt-4o-mini",
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "Extract the string of consecutive digits from this image with length more than 12 digits",
                                    # "text": "Extract the credit card number from this image",
                                },
                                {
                                    "type": "image_url",
                                    "image_url": {"url": data_uri},
                                },
                            ],
                        }
                    ],
                },
            )
        print(f"GPT response = {response.json()}")
        card_number_text = response.json()["choices"][0]["message"]["content"]
        print(f"Extracted text from GPT: {card_number_text}")
        card_number = extract_credit_card_number_from_text(card_number_text)
        print(f"Extracted credit card number: {card_number}")

        # Write the result to the output file (without spaces in the card number)
        with open(output_file_path, "w") as output_file:
            output_file.write(card_number.replace(" ", ""))

        print(f"Extracted credit card number has been written to {output_file_path}")

    except KeyError as e:
        print(
            f"INSIDE EXTRACT_NUMBERS_FROM_IMAGE IN A8. KeyError occurred while querying GPT: {e}"
        )
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        print(
            f"INSIDE EXTRACT_NUMBERS_FROM_IMAGE IN A8. General Error while querying gpt: {str(e)}"
        )
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    input_file_path = "/data/credit_card.png"
    output_file_path = "/data/credit_card_number.txt"

    import asyncio

    asyncio.run(extract_numbers_from_image(input_file_path, output_file_path))
