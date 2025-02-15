# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "requests",
#   "fastapi",
# ]
# ///


import httpx
import os
from typing import Dict, Any
from fastapi import HTTPException
import json


from base_logger import logger


USE_PERSONAL_TOKEN = False

if USE_PERSONAL_TOKEN:
    OPENAI_API_KEY = os.environ["OPENAI_API_MYKEY"]
    # OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
    OPENAI_API_URL = "https://api.openai.com/v1/"

else:
    OPENAI_API_KEY = os.environ["AIPROXY_TOKEN"]
    # OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/"


async def query_gpt(
    user_input: str,
    tools: list[Dict[str, Any]],
    OPENAI_API_KEY: str = "",
    OPENAI_API_URL: str = "",
) -> Dict[str, Any]:
    logger.info(f"Inside query_gpt. User input received = {user_input}")

    if OPENAI_API_KEY == "":
        OPENAI_API_KEY = os.environ["AIPROXY_TOKEN"]

    if OPENAI_API_URL == "":
        OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"

    logger.info(f"Using {OPENAI_API_URL=}")
    logger.info(f"Using {OPENAI_API_KEY=}")

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
            logger.debug(f"Request URL:{response.request.url}")
            logger.info(f"{response.status_code = }")
            response.raise_for_status()
            logger.debug(f"Response from GPT: {json.dumps(response.json(),indent=2)}")
            return response.json()["choices"][0]["message"]["tool_calls"][0]["function"]

    except KeyError as e:
        logger.error(f"KeyError occurred while querying GPT: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        logger.error(f"General Error while querying gpt: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
