import logging
import os


def get_logger(name):


    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)


    os.makedirs("reports/logs", exist_ok=True)


    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


    file_handler = logging.FileHandler("reports/logs/test_run.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger