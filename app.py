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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Allow OPTIONS for preflight requests
    allow_headers=["*"],  # Allow all headers
)


def query_gpt(user_input: str, tools: list[Dict[str, Any]]) -> Dict[str, Any]:
    print(f"Inside query_gpt. User input received = {user_input}")

    try:
        response = httpx.post(
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
        print(f"Response from GPT: {response.json()}")
        return response.json()["choices"][0]["message"]["tool_calls"][0]["function"]

    except KeyError as e:
        print(f"KeyError occurred while querying GPT: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        print(f"General Error while querying gpt: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/run")
async def run_task(task: str):
    print(f"[{now}]Task received:{task}")
    try:
        response = query_gpt(task, tools)

    except Exception as e:
        print(f"Error occurred while querying GPT: {e}")
        raise HTTPException(status_code=404, detail="Error occurred while querying GPT")

    fname = response["name"]
    arguments = response["arguments"]
    arg_dict = json.loads(arguments)

    print(f"Calling function: {fname}")
    print(f"With the below arguments: {arg_dict = }")

    try:
        fun = globals()[fname]
        fun(**arg_dict)
    except Exception as e:
        print(f"Error occurred while calling the function {fname}. Error is: {e}")
        raise HTTPException(
            status_code=500,
            detail="Internal Error occurred while running called the function",
        )

    return JSONResponse(content={"function": fname, "arguments": arg_dict})


from fastapi.responses import PlainTextResponse


@app.get("/read", response_class=PlainTextResponse)
async def read_file(path: str):
    from pathlib import Path

    file_path = Path(path)

    # Check if the file exists and is a file
    if not file_path.is_file():
        raise HTTPException(status_code=404, detail="File not found")

    # Open the file and read its content
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    print(f"{OPENAI_API_KEY=}")

    uvicorn.run(app, host="0.0.0.0", port=8000)
