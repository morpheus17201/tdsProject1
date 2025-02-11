# ///script
# requires-python = ">=3.11"
# dependencies = [
#     markdown,
# ]
# ///





import markdown

from base_logger import logger


def convert_markdown_to_html(input_file_path: str, output_file_path="") -> str:
    logger.info("Inside convert_markdown_to_html function.")
    logger.debug("Arguments received:")
    logger.debug(f"{input_file_path=}")
    logger.debug(f"{output_file_path=}")

    try:
        with open(input_file_path, "r") as file:
            text = file.read()
            logger.debug("File read successfully")
        logger.debug("Converting to html")
        html = markdown.markdown(text)
        logger.debug("Done")
    except Exception as e:
        raise Exception(f"Error occurred while converting markdown to html: {str(e)}")

    if output_file_path != "":
        logger.info(f"Output file path is provided. Writing to {output_file_path}")
        try:
            with open(output_file_path, "w") as file:
                file.write(html)

        except Exception as e:
            raise Exception(f"Error occurred while writing html to file: {str(e)}")

    return html


if __name__ == "__main__":
    convert_markdown_to_html(r"/data/format.md", r"/data/md_to_html.html")
