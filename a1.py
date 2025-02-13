# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
#   "fastapi",
# ]
# ///


import subprocess
import requests
import sys

from fastapi import HTTPException


from base_logger import logger


async def run_datagen_script(
    user_email=r"23f2005138@ds.study.iitm.ac.in",
    script_url=r"https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py",
):
    # Step 1: Download the datagen.py script from the URL
    # script_url = "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py"

    logger.info(f"Parameters received for run_datagen_script:")
    logger.info(f"{user_email=}")
    logger.info(f"{script_url}")

    try:
        response = requests.get(script_url)
        response.raise_for_status()

    except Exception as e:
        logger.critical(
            f"Error occured while fetching the script from the given URL {e}"
        )
        raise HTTPException(status_code=400, detail=str(e))

    script_content = requests.get(script_url).text

    # Step 2: Save the content to a temporary file (datagen.py)
    script_path = "datagen.py"
    with open(script_path, "w") as script_file:
        script_file.write(script_content)

    print("datagen.py downloaded and saved locally.")

    # Step 3: Run the script using subprocess and pass user_email as the argument
    try:
        # subprocess.run([sys.executable, script_path, user_email], check=True)
        subprocess.run(["uv", "run", script_path, user_email], check=True)
        print(f"datagen.py executed successfully with {user_email} as the argument.")
    except subprocess.CalledProcessError as e:
        print(f"Error while running the script: {e}")

    # Clean up by removing the temporary script file


#    try:
#        os.remove(script_path)
#        print("Temporary datagen.py script removed.")
#    except Exception as e:
#        print(f"Error during cleanup: {e}")

# Example usage:

if __name__ == "__main__":
    user_email = "23f2005138@ds.study.iitm.ac.in"  # Replace with actual email
    script_url = "https://url_with_error.com"
    script_url = "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py"
    import asyncio

    asyncio.run(run_datagen_script(user_email, script_url))
