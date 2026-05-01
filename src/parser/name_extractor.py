import re
from src.parser.rut_extractor import extract_rut


def extract_name(text: str) -> str:
    text = (text or "").strip()
    rut = extract_rut(text)
    if rut and rut in text:
        candidate = text.split(rut)[0].strip(" -:\n\t")
        candidate = re.sub(r'\s+', ' ', candidate).strip()
        return candidate
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if lines:
        return lines[0][:120]
    return ""
