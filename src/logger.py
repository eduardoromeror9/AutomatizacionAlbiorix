import logging
from pathlib import Path


def get_logger():
    Path("data/logs").mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("albiorix")
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
    logger.addHandler(handler)
    return logger