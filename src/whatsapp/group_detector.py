def is_probable_group(chat_name: str) -> bool:
    if not chat_name:
        return False
    lowered = chat_name.lower().strip()
    group_indicators = ["turno", "dotacion", "dotación", "local", "sede", "unimarc", "equipo", "grupo"]
    return any(token in lowered for token in group_indicators) or len(lowered.split()) >= 2
