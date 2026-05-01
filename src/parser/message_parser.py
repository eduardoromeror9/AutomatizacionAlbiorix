from src.models import ParsedRecord
from src.parser.keyword_matcher import find_keyword_variants
from src.parser.rut_extractor import extract_rut
from src.parser.name_extractor import extract_name


def parse_message_to_records(message, keywords_config: dict, execution_date: str, expected_date: str = ""):
    if expected_date and message.message_date:
        if message.message_date != expected_date and not message.message_date.endswith(expected_date[-2:]):
            return []

    found = find_keyword_variants(message.message_text, keywords_config)
    if not found:
        return []

    rut = extract_rut(message.message_text)
    name = extract_name(message.message_text)
    records = []

    for category, variant in found:
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

        records.append(ParsedRecord(
            execution_date=execution_date,
            group_name=message.chat_name,
            chat_name=message.chat_name,
            message_date=message.message_date,
            message_time=message.message_time,
            sender=message.sender,
            detected_name=name,
            detected_rut=rut,
            category=category,
            variant=variant,
            status=status,
            message_text=message.message_text,
            notes=notes,
        ))

    return records
