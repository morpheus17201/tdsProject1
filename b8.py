# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "requests",
#   "python-dateutil",
#   "numpy",
##   "faster-whisper",
# ]
# ///

import os
import httpx


async def transcribe_mp3_to_text(mp3_file_path: str) -> str:
    # faster-whisper failed to install through uv or pip
    # Gemini requires API key. How will this API key be passed on to the program?
    # How should the transcribed text be returned? Return as a string or save to file?
    pass
