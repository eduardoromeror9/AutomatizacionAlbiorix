# from src.models import ParsedRecord
# from src.parser.keyword_matcher import find_keyword_variants
# from src.parser.rut_extractor import extract_rut
# from src.parser.name_extractor import extract_name


# def parse_message_to_records(message, keywords_config: dict, execution_date: str, expected_date: str = ""):
#     if expected_date and message.message_date:
#         if message.message_date != expected_date and not message.message_date.endswith(expected_date[-2:]):
#             return []

#     found = find_keyword_variants(message.message_text, keywords_config)
#     if not found:
#         return []

#     rut = extract_rut(message.message_text)
#     name = extract_name(message.message_text)
#     records = []

#     for category, variant in found:
#         status = "OK"
#         notes = ""
#         if not rut and not name:
#             status = "AMBIGUO"
#             notes = "Sin RUT y sin nombre detectado"
#         elif not rut:
#             status = "PALABRA_CLAVE_SIN_RUT"
#             notes = "Se encontró palabra clave, pero no RUT"
#         elif not name:
#             status = "PALABRA_CLAVE_SIN_NOMBRE"
#             notes = "Se encontró palabra clave, pero no nombre"

#         records.append(ParsedRecord(
#             execution_date=execution_date,
#             group_name=message.chat_name,
#             chat_name=message.chat_name,
#             message_date=message.message_date,
#             message_time=message.message_time,
#             sender=message.sender,
#             detected_name=name,
#             detected_rut=rut,
#             category=category,
#             variant=variant,
#             status=status,
#             message_text=message.message_text,
#             notes=notes,
#         ))

#     return records


# import re
# from src.models import ParsedRecord
# from src.parser.keyword_matcher import find_best_keyword_match
# from src.parser.rut_extractor import extract_rut
# from src.parser.name_extractor import extract_name


# def split_candidate_lines(text: str):
#     if not text:
#         return []

#     raw_lines = [line.strip() for line in text.splitlines() if line.strip()]
#     candidate_lines = []

#     for line in raw_lines:
#         compact = re.sub(r'\s+', ' ', line).strip()

#         if len(compact) < 8:
#             continue

#         candidate_lines.append(compact)

#     return candidate_lines


# def line_looks_like_record(line: str, keywords_config: dict):
#     has_rut = bool(extract_rut(line))
#     keyword_match = find_best_keyword_match(line, keywords_config)

#     if has_rut and keyword_match:
#         return True

#     return False


# def parse_message_to_records(message, keywords_config: dict, execution_date: str, expected_date: str = ""):
#     if expected_date and message.message_date:
#         if message.message_date != expected_date and not message.message_date.endswith(expected_date[-2:]):
#             return []

#     lines = split_candidate_lines(message.message_text)
#     records = []
#     seen = set()

#     for line in lines:
#         if not line_looks_like_record(line, keywords_config):
#             continue

#         keyword_match = find_best_keyword_match(line, keywords_config)
#         if not keyword_match:
#             continue

#         category, variant = keyword_match
#         rut = extract_rut(line)
#         name = extract_name(line)

#         status = "OK"
#         notes = ""

#         if not rut and not name:
#             status = "AMBIGUO"
#             notes = "Sin RUT y sin nombre detectado"
#         elif not rut:
#             status = "PALABRA_CLAVE_SIN_RUT"
#             notes = "Se encontró palabra clave, pero no RUT"
#         elif not name:
#             status = "PALABRA_CLAVE_SIN_NOMBRE"
#             notes = "Se encontró palabra clave, pero no nombre"

#         dedupe_key = (
#             message.chat_name.strip().lower(),
#             message.message_date.strip(),
#             message.message_time.strip(),
#             line.strip().lower(),
#             category.strip().lower(),
#             variant.strip().lower(),
#         )

#         if dedupe_key in seen:
#             continue
#         seen.add(dedupe_key)

#         records.append(
#             ParsedRecord(
#                 execution_date=execution_date,
#                 group_name=message.chat_name,
#                 chat_name=message.chat_name,
#                 message_date=message.message_date,
#                 message_time=message.message_time,
#                 sender=message.sender,
#                 detected_name=name,
#                 detected_rut=rut,
#                 category=category,
#                 variant=variant,
#                 status=status,
#                 message_text=line,
#                 notes=notes,
#             )
#         )

#     return records

# import re
# from src.models import ParsedRecord
# from src.parser.keyword_matcher import find_best_keyword_match
# from src.parser.rut_extractor import extract_rut
# from src.parser.name_extractor import extract_name


# def split_candidate_lines(text: str):
#     if not text:
#         return []
#     return [re.sub(r'\s+', ' ', line).strip() for line in text.splitlines() if line.strip() and len(line.strip()) >= 8]


# def expand_compact_segments(text: str):
#     if not text:
#         return []
#     normalized = re.sub(r'\s+', ' ', text).strip()
#     pattern = re.compile(
#         r'(?P<name>[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+(?:\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+){1,4})\s+'
#         r'(?P<rut>\d{1,2}\.?\d{3}\.?\d{3}-[\dkK])\s+'
#         r'(?P<tail>[^\n]*?)(?=(?:\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+\s+\d{1,2}\.?\d{3}\.?\d{3}-[\dkK])|$)'
#     )
#     segments = [f"{m.group('name')} {m.group('rut')} {m.group('tail').strip()}" for m in pattern.finditer(normalized)]
#     return segments


# def line_looks_like_record(line: str, keywords_config: dict):
#     return bool(extract_rut(line) and find_best_keyword_match(line, keywords_config))


# def parse_message_to_records(message, keywords_config: dict, execution_date: str, expected_date: str = ""):
#     if expected_date and message.message_date:
#         if message.message_date != expected_date and not message.message_date.endswith(expected_date[-2:]):
#             return []

#     base_lines = split_candidate_lines(message.message_text)
#     lines = []
#     for line in base_lines:
#         expanded = expand_compact_segments(line)
#         lines.extend(expanded if expanded else [line])

#     records, seen = [], set()
#     for line in lines:
#         if not line_looks_like_record(line, keywords_config):
#             continue
#         match = find_best_keyword_match(line, keywords_config)
#         if not match:
#             continue
#         category, variant = match
#         rut = extract_rut(line)
#         name = extract_name(line)
#         status, notes = "OK", ""
#         if not rut and not name:
#             status, notes = "AMBIGUO", "Sin RUT y sin nombre detectado"
#         elif not rut:
#             status, notes = "PALABRA_CLAVE_SIN_RUT", "Se encontró palabra clave, pero no RUT"
#         elif not name:
#             status, notes = "PALABRA_CLAVE_SIN_NOMBRE", "Se encontró palabra clave, pero no nombre"
#         dedupe_key = (message.chat_name.strip().lower(), message.message_date.strip(), message.message_time.strip(), line.strip().lower(), category.strip().lower(), variant.strip().lower())
#         if dedupe_key in seen:
#             continue
#         seen.add(dedupe_key)
#         records.append(ParsedRecord(execution_date=execution_date, group_name=message.chat_name, chat_name=message.chat_name, message_date=message.message_date, message_time=message.message_time, sender=message.sender, detected_name=name, detected_rut=rut, category=category, variant=variant, status=status, message_text=line, notes=notes))
#     return records


# import re
# from src.models import ParsedRecord
# from src.parser.keyword_matcher import find_best_keyword_match
# from src.parser.rut_extractor import extract_rut
# from src.parser.name_extractor import extract_name
# from src.parser.location_extractor import extract_local_and_comuna


# HEADER_PATTERN = re.compile(
#     r"dotaci[oó]n\s+turno\s+(?:am|pm)\s+\d{1,2}-\d{1,2}-\d{4}\s+(.*)",
#     re.IGNORECASE
# )

# def split_candidate_lines(text: str):
#     if not text:
#         return []
#     return [
#         re.sub(r"\s+", " ", line).strip()
#         for line in text.splitlines()
#         if line.strip() and len(line.strip()) >= 8
#     ]

# def expand_compact_segments(text: str):
#     if not text:
#         return []
#     normalized = re.sub(r"\s+", " ", text).strip()
#     pattern = re.compile(
#         r'(?P<name>[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+(?:\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+){1,4})\s+'
#         r'(?P<rut>\d{1,2}\.?\d{3}\.?\d{3}-[\dkK])\s+'
#         r'(?P<tail>[^\n]*?)(?=(?:\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+\s+\d{1,2}\.?\d{3}\.?\d{3}-[\dkK])|$)'
#     )
#     return [
#         f"{m.group('name')} {m.group('rut')} {m.group('tail').strip()}"
#         for m in pattern.finditer(normalized)
#     ]

# def extract_location_from_message(message_text: str):
#     for line in split_candidate_lines(message_text):
#         match = HEADER_PATTERN.search(line)
#         if match:
#             header_tail = match.group(1).strip()
#             local, comuna = extract_local_and_comuna(header_tail)
#             return local, comuna
#     return "", ""

# def line_looks_like_record(line: str, keywords_config: dict):
#     return bool(extract_rut(line) and find_best_keyword_match(line, keywords_config))

# def parse_message_to_records(message, keywords_config: dict, execution_date: str, expected_date: str = ""):
#     if expected_date and message.message_date:
#         if message.message_date != expected_date and not message.message_date.endswith(expected_date[-2:]):
#             return []

#     local, comuna = extract_location_from_message(message.message_text)

#     base_lines = split_candidate_lines(message.message_text)
#     lines = []
#     for line in base_lines:
#         expanded = expand_compact_segments(line)
#         lines.extend(expanded if expanded else [line])

#     records, seen = [], set()

#     for line in lines:
#         if not line_looks_like_record(line, keywords_config):
#             continue

#         match = find_best_keyword_match(line, keywords_config)
#         if not match:
#             continue

#         category, variant = match
#         rut = extract_rut(line)
#         name = extract_name(line)

#         status, notes = "OK", ""

#         if not rut and not name:
#             status, notes = "AMBIGUO", "Sin RUT y sin nombre detectado"
#         elif not rut:
#             status, notes = "PALABRA_CLAVE_SIN_RUT", "Se encontró palabra clave, pero no RUT"
#         elif not name:
#             status, notes = "PALABRA_CLAVE_SIN_NOMBRE", "Se encontró palabra clave, pero no nombre"

#         dedupe_key = (
#             message.chat_name.strip().lower(),
#             message.message_date.strip(),
#             message.message_time.strip(),
#             line.strip().lower(),
#             category.strip().lower(),
#             variant.strip().lower()
#         )

#         if dedupe_key in seen:
#             continue
#         seen.add(dedupe_key)

#         records.append(
#             ParsedRecord(
#                 execution_date=execution_date,
#                 group_name=message.chat_name,
#                 chat_name=message.chat_name,
#                 message_date=message.message_date,
#                 message_time=message.message_time,
#                 sender=message.sender,
#                 detected_name=name,
#                 detected_rut=rut,
#                 category=category,
#                 variant=variant,
#                 status=status,
#                 message_text=line,
#                 notes=notes,
#                 local=local,
#                 comuna=comuna
#             )
#         )

#     return records

# import re
# from src.models import ParsedRecord
# from src.parser.keyword_matcher import find_best_keyword_match
# from src.parser.rut_extractor import extract_rut
# from src.parser.name_extractor import extract_name

# HEADER_PATTERN = re.compile(
#     r"^\s*dotaci[oó]n\s+turno\s+(?:am|pm)\s+\d{1,2}-\d{1,2}-\d{4}\s+(?P<location>.+?)\s*$",
#     re.IGNORECASE
# )

# def normalize_spaces(text: str):
#     return re.sub(r"\s+", " ", (text or "").strip())

# def split_candidate_lines(text: str):
#     if not text:
#         return []
#     return [normalize_spaces(line) for line in text.splitlines() if line.strip() and len(line.strip()) >= 8]

# def expand_compact_segments(text: str):
#     if not text:
#         return []
#     normalized = normalize_spaces(text)
#     pattern = re.compile(
#         r'(?P<name>[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+(?:\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+){1,4})\s+'
#         r'(?P<rut>\d{1,2}\.?\d{3}\.?\d{3}-[\dkK])\s+'
#         r'(?P<tail>[^\n]*?)(?=(?:\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+\s+\d{1,2}\.?\d{3}\.?\d{3}-[\dkK])|$)'
#     )
#     return [f"{m.group('name')} {m.group('rut')} {m.group('tail').strip()}" for m in pattern.finditer(normalized)]

# def extract_location_from_block(header_line: str):
#     match = HEADER_PATTERN.match(header_line or "")
#     if not match:
#         return "", ""
#     raw_location = normalize_spaces(match.group("location"))
#     parts = raw_location.split()
#     if len(parts) < 2:
#         return raw_location, ""
#     return " ".join(parts[:-1]), parts[-1]

# def line_looks_like_record(line: str, keywords_config: dict):
#     return bool(extract_rut(line) and find_best_keyword_match(line, keywords_config))

# def parse_message_to_records(message, keywords_config: dict, execution_date: str, expected_date: str = ""):
#     if expected_date and message.message_date:
#         if message.message_date != expected_date and not message.message_date.endswith(expected_date[-2:]):
#             return []

#     lines = split_candidate_lines(message.message_text)
#     records = []
#     seen = set()

#     current_local = ""
#     current_comuna = ""

#     for raw_line in lines:
#         header_match = HEADER_PATTERN.match(raw_line)
#         if header_match:
#             current_local, current_comuna = extract_location_from_block(raw_line)
#             continue

#         expanded = expand_compact_segments(raw_line)
#         candidate_lines = expanded if expanded else [raw_line]

#         for line in candidate_lines:
#             if not line_looks_like_record(line, keywords_config):
#                 continue

#             match = find_best_keyword_match(line, keywords_config)
#             if not match:
#                 continue

#             category, variant = match
#             rut = extract_rut(line)
#             name = extract_name(line)

#             status = "OK"
#             notes = ""

#             if not rut and not name:
#                 status = "AMBIGUO"
#                 notes = "Sin RUT y sin nombre detectado"
#             elif not rut:
#                 status = "PALABRA_CLAVE_SIN_RUT"
#                 notes = "Se encontró palabra clave, pero no RUT"
#             elif not name:
#                 status = "PALABRA_CLAVE_SIN_NOMBRE"
#                 notes = "Se encontró palabra clave, pero no nombre"

#             dedupe_key = (
#                 message.chat_name.strip().lower(),
#                 message.message_date.strip(),
#                 message.message_time.strip(),
#                 line.strip().lower(),
#                 category.strip().lower(),
#                 variant.strip().lower(),
#                 current_local.strip().lower(),
#                 current_comuna.strip().lower(),
#             )

#             if dedupe_key in seen:
#                 continue
#             seen.add(dedupe_key)

#             records.append(
#                 ParsedRecord(
#                     execution_date=execution_date,
#                     group_name=message.chat_name,
#                     chat_name=message.chat_name,
#                     message_date=message.message_date,
#                     message_time=message.message_time,
#                     sender=message.sender,
#                     detected_name=name,
#                     detected_rut=rut,
#                     category=category,
#                     variant=variant,
#                     status=status,
#                     message_text=line,
#                     notes=notes,
#                     local=current_local,
#                     comuna=current_comuna,
#                 )
#             )

#     return records

# import re
# from src.models import ParsedRecord
# from src.parser.keyword_matcher import find_best_keyword_match
# from src.parser.rut_extractor import extract_rut
# from src.parser.name_extractor import extract_name
# from src.parser.location_extractor import extract_local_and_comuna

# HEADER_PATTERN = re.compile(
#     r"^\s*dotaci[oó]n\s+turno\s+(?:am|pm)\s+\d{1,2}-\d{1,2}-\d{4}\s+(?P<tail>.+?)\s*$",
#     re.IGNORECASE
# )

# def normalize_spaces(text: str):
#     return re.sub(r"\s+", " ", (text or "").strip())

# def split_candidate_lines(text: str):
#     if not text:
#         return []
#     return [normalize_spaces(line) for line in text.splitlines() if line.strip() and len(line.strip()) >= 8]

# def expand_compact_segments(text: str):
#     if not text:
#         return []
#     normalized = normalize_spaces(text)
#     pattern = re.compile(
#         r'(?P<name>[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+(?:\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+){1,4})\s+'
#         r'(?P<rut>\d{1,2}\.?\d{3}\.?\d{3}-[\dkK])\s+'
#         r'(?P<tail>[^\n]*?)(?=(?:\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+\s+\d{1,2}\.?\d{3}\.?\d{3}-[\dkK])|$)'
#     )
#     return [f"{m.group('name')} {m.group('rut')} {m.group('tail').strip()}" for m in pattern.finditer(normalized)]

# def extract_location_from_header(line: str):
#     match = HEADER_PATTERN.match(line or "")
#     if not match:
#         return "", ""
#     return extract_local_and_comuna(match.group("tail"))

# def line_looks_like_record(line: str, keywords_config: dict):
#     return bool(extract_rut(line) and find_best_keyword_match(line, keywords_config))

# def parse_message_to_records(message, keywords_config: dict, execution_date: str, expected_date: str = ""):
#     if expected_date and message.message_date:
#         if message.message_date != expected_date and not message.message_date.endswith(expected_date[-2:]):
#             return []

#     lines = split_candidate_lines(message.message_text)
#     records = []
#     seen = set()
#     current_local = ""
#     current_comuna = ""

#     for raw_line in lines:
#         header_match = HEADER_PATTERN.match(raw_line)
#         if header_match:
#             current_local, current_comuna = extract_location_from_header(raw_line)
#             continue

#         expanded = expand_compact_segments(raw_line)
#         candidate_lines = expanded if expanded else [raw_line]

#         for line in candidate_lines:
#             if not line_looks_like_record(line, keywords_config):
#                 continue

#             match = find_best_keyword_match(line, keywords_config)
#             if not match:
#                 continue

#             category, variant = match
#             rut = extract_rut(line)
#             name = extract_name(line)

#             status = "OK"
#             notes = ""

#             if not rut and not name:
#                 status = "AMBIGUO"
#                 notes = "Sin RUT y sin nombre detectado"
#             elif not rut:
#                 status = "PALABRA_CLAVE_SIN_RUT"
#                 notes = "Se encontró palabra clave, pero no RUT"
#             elif not name:
#                 status = "PALABRA_CLAVE_SIN_NOMBRE"
#                 notes = "Se encontró palabra clave, pero no nombre"

#             dedupe_key = (
#                 message.chat_name.strip().lower(),
#                 message.message_date.strip(),
#                 message.message_time.strip(),
#                 line.strip().lower(),
#                 category.strip().lower(),
#                 variant.strip().lower(),
#                 current_local.strip().lower(),
#                 current_comuna.strip().lower(),
#             )

#             if dedupe_key in seen:
#                 continue
#             seen.add(dedupe_key)

#             records.append(
#                 ParsedRecord(
#                     execution_date=execution_date,
#                     group_name=message.chat_name,
#                     chat_name=message.chat_name,
#                     message_date=message.message_date,
#                     message_time=message.message_time,
#                     sender=message.sender,
#                     detected_name=name,
#                     detected_rut=rut,
#                     category=category,
#                     variant=variant,
#                     status=status,
#                     message_text=line,
#                     notes=notes,
#                     local=current_local,
#                     comuna=current_comuna,
#                 )
#             )

#     return records

import re
from src.models import ParsedRecord
from src.parser.keyword_matcher import find_best_keyword_match
from src.parser.rut_extractor import extract_rut
from src.parser.name_extractor import extract_name
from src.parser.location_extractor import extract_local_and_comuna

HEADER_PATTERN = re.compile(
    r"^\s*dotaci[oó]n\s+turno\s+(?:am|pm)\s+(?P<date>\d{1,2}-\d{1,2}-\d{4})(?:\s+(?P<tail>.+))?$",
    re.IGNORECASE
)

DATE_IN_BODY_PATTERN = re.compile(r"\b\d{1,2}-\d{1,2}-\d{4}\b")


def normalize_spaces(text: str):
    return re.sub(r"\s+", " ", (text or "").strip())


def split_candidate_lines(text: str):
    if not text:
        return []
    return [normalize_spaces(line) for line in text.splitlines() if line.strip() and len(line.strip()) >= 8]


def expand_compact_segments(text: str):
    if not text:
        return []
    normalized = normalize_spaces(text)
    pattern = re.compile(
        r'(?P<name>[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+(?:\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+){1,4})\s+'
        r'(?P<rut>\d{1,2}\.?(?:\d{3}\.?)?\d{3}-[\dkK])\s+'
        r'(?P<tail>[^\n]*?)(?=(?:\s+[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\-]+\s+\d{1,2}\.?(?:\d{3}\.?)?\d{3}-[\dkK])|$)'
    )
    return [f"{m.group('name')} {m.group('rut')} {m.group('tail').strip()}" for m in pattern.finditer(normalized)]


def extract_header_context(line: str):
    match = HEADER_PATTERN.match(line or "")
    if not match:
        return "", "", ""
    date = match.group("date") or ""
    tail = match.group("tail") or ""
    local, comuna = extract_local_and_comuna(tail)
    return date, local, comuna


def line_looks_like_record(line: str, keywords_config: dict):
    return bool(extract_rut(line) and find_best_keyword_match(line, keywords_config))


def parse_message_to_records(message, keywords_config: dict, execution_date: str, expected_date: str = ""):
    lines = split_candidate_lines(message.message_text)
    records = []
    seen = set()
    current_local = ""
    current_comuna = ""
    current_date = expected_date or message.message_date or ""

    for raw_line in lines:
        header_match = HEADER_PATTERN.match(raw_line)
        if header_match:
            current_date, current_local, current_comuna = extract_header_context(raw_line)
            continue

        if DATE_IN_BODY_PATTERN.search(raw_line) and raw_line.lower().startswith("dotación turno"):
            current_date, current_local, current_comuna = extract_header_context(raw_line)
            continue

        expanded = expand_compact_segments(raw_line)
        candidate_lines = expanded if expanded else [raw_line]

        for line in candidate_lines:
            if not line_looks_like_record(line, keywords_config):
                continue

            match = find_best_keyword_match(line, keywords_config)
            if not match:
                continue

            category, variant = match
            rut = extract_rut(line)
            name = extract_name(line)

            status = "OK"
            notes = ""

            if not rut and not name:
                status = "AMBIGUO"
                notes = "Sin RUT y sin nombre detectado"
            elif not rut:
                status = "PALABRA_CLAVE_SIN_RUT"
                notes = "Se encontró palabra clave, pero no RUT"
            elif not name:
                status = "PALABRA_CLAVE_SIN_NOMBRE"
                notes = "Se encontró palabra clave, pero no nombre"

            dedupe_key = (
                message.chat_name.strip().lower(),
                current_date.strip().lower(),
                line.strip().lower(),
                category.strip().lower(),
                variant.strip().lower(),
                current_local.strip().lower(),
                current_comuna.strip().lower(),
                rut.strip().lower(),
                name.strip().lower(),
            )

            if dedupe_key in seen:
                continue
            seen.add(dedupe_key)

            records.append(
                ParsedRecord(
                    execution_date=execution_date,
                    group_name=message.chat_name,
                    chat_name=message.chat_name,
                    message_date=current_date or message.message_date,
                    message_time=message.message_time,
                    sender=message.sender,
                    detected_name=name,
                    detected_rut=rut,
                    category=category,
                    variant=variant,
                    status=status,
                    message_text=line,
                    notes=notes,
                    local=current_local,
                    comuna=current_comuna,
                )
            )

    return records