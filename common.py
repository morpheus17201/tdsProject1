# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "requests",
# ]
# ///


import httpx
import os
from typing import Dict, Any

from base_logger import logger


async def query_gpt(user_input: str, tools: list[Dict[str, Any]]) -> Dict[str, Any]:
    logger.info(f"Inside query_gpt. User input received = {user_input}")

    OPENAI_API_KEY = os.environ["AIPROXY_TOKEN"]
    OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"

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
            logger.debug(f"Response from GPT: {response.json()}")
            return response.json()["choices"][0]["message"]["tool_calls"][0]["function"]

    except KeyError as e:
        logger.error(f"KeyError occurred while querying GPT: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        logger.error(f"General Error while querying gpt: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
