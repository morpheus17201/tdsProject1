# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "fastapi",
#   "uvicorn",
#   "requests",
#   "python-dateutil",
#   "numpy",
# ]
# ///

import httpx
from typing import Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import datetime
import os
import json
import logging

from a1 import run_datagen_script
from a2 import format_file_with_prettier
from a3 import count_given_weekday_in_dates
from a4 import sort_contacts_file
from a5 import write_most_recent_log_first_lines
from a6 import extract_titles_from_markdown_files
from a7 import extract_sender_email
from a9 import get_similar_comments
from a8 import extract_numbers_from_image
from a10 import calculate_ticket_sales


from tools_definition import tools

# A1 task is to download all data files.
# Hence this has to be run irrespective of
# all other tasks
user_email = "23f2005138@ds.study.iitm.ac.in"
# run_datagen_script(user_email=user_email)

now = datetime.datetime.now()

OPENAI_API_KEY = os.environ["AIPROXY_TOKEN"]
OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"


# Initialize the FastAPI app
app = FastAPI()

# CORS Configuration (Allow all origins and headers)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "OPTIONS"],  # Allow OPTIONS for preflight requests
#     allow_headers=["*"],  # Allow all headers
# )


async def query_gpt(user_input: str, tools: list[Dict[str, Any]]) -> Dict[str, Any]:
    logging.info(f"Inside query_gpt. User input received = {user_input}")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                OPENAI_API_URL,
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "gpt-4o-mini",
                    "messages": [{"role": "user", "content": user_input}],
                    "tools": tools,
                    "tool_choice": "auto",
                },
            )
            print(f"{response.status_code = }")
            response.raise_for_status()
            logging.debug(f"Response from GPT: {response.json()}")
            return response.json()["choices"][0]["message"]["tool_calls"][0]["function"]

    except KeyError as e:
        logging.error(f"KeyError occurred while querying GPT: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        logging.error(f"General Error while querying gpt: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/run")
async def run_task(task: str):
    print(" " * 80)
    print("=" * 80)
    print(" " * 80)
    logging.info(f"[{now}]Task received:{task}")
    try:
        response = await query_gpt(task, tools)

    except Exception as e:
        logging.error(f"Error occurred while querying GPT: {e}")
        raise HTTPException(status_code=404, detail="Error occurred while querying GPT")

    fname = response["name"]
    arguments = response["arguments"]
    arg_dict = json.loads(arguments)

    # print(f"Calling function: {fname}")
    # print(f"With the below arguments: {arg_dict = }")

    arg_dict_str = ", ".join([f"{k}='{v}'" for k, v in arg_dict.items()])
    print("-" * 80)
    logging.info(f"Calling function: {fname}({arg_dict_str})")

    try:
        fun = globals()[fname]
        await fun(**arg_dict)
    except Exception as e:
        logging.error(
            f"Error occurred while calling the function {fname}. Error is: {e}"
        )
        raise HTTPException(
            status_code=500,
            detail="Internal Error occurred while running called the function",
        )
    print("-" * 80)
    return JSONResponse(content={"function": fname, "arguments": arg_dict})


from fastapi.responses import PlainTextResponse


@app.get("/read", response_class=PlainTextResponse)
async def read_file(path: str):
    print("-" * 80)
    from pathlib import Path

    file_path = Path(path)

    # Check if the file exists and is a file
    if not file_path.is_file():
        logging.error(f"File not found: {file_path}")
        raise HTTPException(status_code=404, detail="File not found")

    # Open the file and read its content
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except Exception as e:
        logging.error(f"Exception from inside app.get('/read')")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    logging.basicConfig(level="INFO", format="%(message)s\n")
    logging.debug(f"{OPENAI_API_KEY=}")

    uvicorn.run(app, host="0.0.0.0", port=8000)
