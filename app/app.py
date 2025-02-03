# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "fastapi",
#   "uvicorn"
# ]
# ///

import httpx
from typing import Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import datetime
import os


from a2 import format_file_with_prettier
from a3 import count_wednesdays_in_dates

from app.tools_definition import tools

now = datetime.datetime.now()

OPENAI_API_KEY = os.environ("OPENAI_API_KEY")
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
    print(f"Inside query_gpt")
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
    # print(f"Response from GPT: {response.json()}")
    return response.json()["choices"][0]["message"]


@app.post("/run")
async def run_task(task: str):
    print(f"[{now}]Task received:{q}")
    response = query_gpt(task, tools)
    # print([tool_call["function"] for tool_call in response["tool_calls"]])
    return response["tool_calls"][0]["function"]


@app.get("/read")
async def read_file(path: str):
    pass
