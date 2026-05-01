import re
import unicodedata


def strip_accents(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn")


def normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()
