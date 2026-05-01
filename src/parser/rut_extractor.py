import re

RUT_PATTERN = re.compile(r'\b\d{1,2}\.?\d{3}\.?\d{3}-[\dkK]\b')


def extract_rut(text: str) -> str:
    match = RUT_PATTERN.search(text or "")
    return match.group(0) if match else ""
