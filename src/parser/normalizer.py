import re
import unicodedata


def strip_accents(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", text or "") if unicodedata.category(c) != "Mn")


def normalize_text(text: str) -> str:
    text = (text or "").lower()
    text = strip_accents(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
