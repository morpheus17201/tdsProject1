# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "fastapi",
#   "uvicorn",
#   "requests"
# ]
# ///

import httpx
from typing import Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import datetime
import os

from a1 import run_datagen_script
from a2 import format_file_with_prettier
from a3 import count_wednesdays_in_dates

from tools_definition import tools

# A1 task is to download all data files.
# Hence this has to be run irrespective of
# all other tasks
user_email = "23f2005138@ds.study.iitm.ac.in"
run_datagen_script(user_email=user_email)

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
        print(f"Response from GPT: {response.json()}")
        return response.json()["choices"][0]["message"]

    except KeyError as e:
        print(f"KeyError while querying gpt: {str(e)}")

    except Exception as e:
        print(f"General Error while querying gpt: {str(e)}")


@app.post("/run")
async def run_task(task: str):
    print(f"[{now}]Task received:{task}")
    response = query_gpt(task, tools)
    # print([tool_call["function"] for tool_call in response["tool_calls"]])
    return response["tool_calls"][0]["function"]


@app.get("/read")
async def read_file(path: str):
    pass


if __name__ == "__main__":
    import uvicorn

    print(f"{OPENAI_API_KEY=}")

    uvicorn.run(app, host="0.0.0.0", port=8000)
