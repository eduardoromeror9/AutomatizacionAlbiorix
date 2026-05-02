# import re
# from src.parser.rut_extractor import extract_rut


# def extract_name(text: str) -> str:
#     text = (text or "").strip()
#     rut = extract_rut(text)
#     if rut and rut in text:
#         candidate = text.split(rut)[0].strip(" -:\n\t")
#         candidate = re.sub(r'\s+', ' ', candidate).strip()
#         return candidate
#     lines = [line.strip() for line in text.splitlines() if line.strip()]
#     if lines:
#         return lines[0][:120]
#     return ""


# import re
# from src.parser.rut_extractor import extract_rut

# HEADER_WORDS = [
#     "dotacion", "dotación", "turno", "am", "pm"
# ]


# def extract_name(text: str) -> str:
#     text = (text or "").strip()
#     rut = extract_rut(text)

#     if not text:
#         return ""

#     if rut and rut in text:
#         left = text.split(rut)[0].strip(" -:\n\t")
#     else:
#         left = text

#     left = re.sub(r'\s+', ' ', left).strip()

#     tokens = left.split()
#     cleaned_tokens = []
#     for token in tokens:
#         if token.lower() not in HEADER_WORDS:
#             cleaned_tokens.append(token)

#     cleaned = " ".join(cleaned_tokens).strip()

#     date_pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b'
#     cleaned = re.sub(date_pattern, '', cleaned).strip()
#     cleaned = re.sub(r'\s+', ' ', cleaned).strip()

#     return cleaned[:120]


# import re
# from src.parser.rut_extractor import extract_rut

# HEADER_WORDS = {"dotacion", "dotación", "turno", "am", "pm"}


# def extract_name(text: str) -> str:
#     text = (text or "").strip()
#     rut = extract_rut(text)
#     left = text.split(rut)[0].strip(" -:\n\t") if rut and rut in text else text
#     left = re.sub(r'\s+', ' ', left).strip()
#     tokens = [t for t in left.split() if t.lower() not in HEADER_WORDS]
#     cleaned = ' '.join(tokens)
#     cleaned = re.sub(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b', '', cleaned).strip()
#     cleaned = re.sub(r'\s+', ' ', cleaned).strip()
#     return cleaned[:120]

import re


def extract_name(text: str):
    if not text:
        return ""
    m = re.match(r"^([A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+(?:\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+){1,4})\s+", text.strip())
    return m.group(1).strip() if m else ""