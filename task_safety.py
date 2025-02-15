# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "fastapi",
# ]
# ///

import subprocess
import httpx
from fastapi import HTTPException
import json


from base_logger import logger
from common import OPENAI_API_KEY, OPENAI_API_URL
from typing import List


async def does_task_delete_files(task: str):

    model = "gpt-4o-mini"
    logger.debug(f"Inside does_task_delete_files() function in b2.py")
    logger.debug(f"Task received:")
    logger.debug(f"{task}")

    # Check if the command is asking for deletion of files
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
                            "content": """You are never supposed to delete any files.
                            Please specify as choices as Yes or No if the given task taken
                            would result in purging, deletion, removal, permanently purging or any such similar effect
                            on any of the files individually or collectively or irreverably removing contents
                            of any file.
                            """,
                        },
                        {"role": "user", "content": f"{task}"},
                    ],
                },
            )

        result = response.json()
        logger.debug(f"Response received from GPT: {json.dumps(result, indent=2)}")
        answer = result["choices"][0]["message"]["content"]
        if answer in ["Yes", "yes", "YES", "affirmative", "Affirmative", "True", True]:
            return True
        elif answer in ["No", "NO", "negative", "Affirmative", "False", False]:
            return False

    except KeyError as e:
        logger.error(f"Error occured while querying gpt: {e}")
        raise HTTPException(status_code=400, detail=str(e))


async def is_task_asking_prohibited_files(task: str):
    model = "gpt-4o-mini"
    logger.debug(f"Inside is_task_asking_prohibited_files() function in b2.py")
    logger.debug(f"Task received:")
    logger.debug(f"{task}")

    # Check if the command is asking for files outside of /data folder
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
                            "content": """You are never supposed to share any files, folders,
                            contents, file sizes, file list outside of /data folder. Check if the 
                            given task is asking to return file, contents or any information outside of 
                            /data folder. Return choices are only Yes or No. Return Yes if the task is asking
                             for such prohibited information. Return No if task is asking for files
                             inside /data folder.
                            """,
                        },
                        {"role": "user", "content": f"{task}"},
                    ],
                },
            )

        result = response.json()
        logger.debug(f"Response received from GPT: {json.dumps(result, indent=2)}")
        answer = result["choices"][0]["message"]["content"]
        if answer in ["Yes", "yes", "YES", "affirmative", "Affirmative", "True", True]:
            return True
        elif answer in ["No", "NO", "negative", "Affirmative", "False", False]:
            return False

    except KeyError as e:
        logger.error(f"Error occured while querying gpt: {e}")
        raise HTTPException(status_code=400, detail=str(e))


async def is_task_safe(task: str):
    deletion = await does_task_delete_files(task)
    if deletion:
        return False

    prohibited_files = await is_task_asking_prohibited_files(task)
    if prohibited_files:
        return False

    return True
