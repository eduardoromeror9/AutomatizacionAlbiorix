# import re

# RUT_PATTERN = re.compile(r'\b\d{1,2}\.?\d{3}\.?\d{3}-[\dkK]\b')


# def extract_rut(text: str) -> str:
#     match = RUT_PATTERN.search(text or "")
#     return match.group(0) if match else ""


import re


def extract_rut(text: str):
    if not text:
        return ""
    m = re.search(r"(\d{1,2}\.\d{3}\.\d{3}-[\dkK]|\d{7,8}-[\dkK])", text)
    return m.group(1) if m else ""