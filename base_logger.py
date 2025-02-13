import logging

# Create a logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Create a formatter to define the log format
FORMAT = "[%(asctime)s - %(levelname)s - %(funcName)20s(): ] %(message)s"
# formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
formatter = logging.Formatter(FORMAT)


# Create a file handler to write logs to a file
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Create a stream handler to print logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(
    logging.DEBUG
)  # You can set the desired log level for console output
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Now you can log messages with different levels
logger.info("Starting logger")
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
