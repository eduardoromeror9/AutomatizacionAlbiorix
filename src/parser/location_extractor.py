# import re

# KNOWN_COMMUNAS = [
#     "Alhué", "Buin", "Calera de Tango", "Cerrillos", "Cerro Navia", "Colina",
#     "Conchalí", "Curacaví", "El Bosque", "El Monte", "Estación Central",
#     "Huechuraba", "Independencia", "Isla de Maipo", "La Cisterna", "La Florida",
#     "La Granja", "La Pintana", "La Reina", "Lampa", "Las Condes", "Lo Barnechea",
#     "Lo Espejo", "Lo Prado", "Macul", "Maipú", "María Pinto", "Melipilla",
#     "Ñuñoa", "Padre Hurtado", "Paine", "Pedro Aguirre Cerda", "Peñaflor",
#     "Peñalolén", "Pirque", "Providencia", "Pudahuel", "Puente Alto", "Quilicura",
#     "Quinta Normal", "Recoleta", "Renca", "San Bernardo", "San Joaquín",
#     "San José de Maipo", "San Miguel", "San Pedro", "San Ramón", "Santiago",
#     "Talagante", "Tiltil", "Vitacura"
# ]

# def normalize_text(text: str) -> str:
#     text = (text or "").strip()
#     text = re.sub(r"\s+", " ", text)
#     return text

# def normalize_spaces(text: str) -> str:
#     return re.sub(r"\s+", " ", (text or "").strip())

# def extract_local_and_comuna(header_tail: str):
#     text = normalize_text(header_tail)
#     if not text:
#         return "", ""

#     parts = text.split()
#     if len(parts) < 2:
#         return text, ""

#     lower_text = text.lower()

#     best_communa = ""
#     best_index = -1

#     for comuna in sorted(KNOWN_COMMUNAS, key=len, reverse=True):
#         idx = lower_text.rfind(comuna)
#         if idx != -1 and idx > best_index:
#             best_index = idx
#             best_communa = comuna

#     if best_communa:
#         local = text[:best_index].strip(" -")
#         comuna_text = text[best_index:].strip(" -")
#         return local, comuna_text.title()

#     if len(parts) >= 2:
#         local = " ".join(parts[:-1]).strip()
#         comuna = parts[-1].strip()
#         return local, comuna

#     return text, ""

# import re

# KNOWN_COMMUNAS = [
#     "Alhué", "Buin", "Calera de Tango", "Cerrillos", "Cerro Navia", "Colina",
#     "Conchalí", "Curacaví", "El Bosque", "El Monte", "Estación Central",
#     "Huechuraba", "Independencia", "Isla de Maipo", "La Cisterna", "La Florida",
#     "La Granja", "La Pintana", "La Reina", "Lampa", "Las Condes", "Lo Barnechea",
#     "Lo Espejo", "Lo Prado", "Macul", "Maipú", "María Pinto", "Melipilla",
#     "Ñuñoa", "Padre Hurtado", "Paine", "Pedro Aguirre Cerda", "Peñaflor",
#     "Peñalolén", "Pirque", "Providencia", "Pudahuel", "Puente Alto", "Quilicura",
#     "Quinta Normal", "Recoleta", "Renca", "San Bernardo", "San Joaquín",
#     "San José de Maipo", "San Miguel", "San Pedro", "San Ramón", "Santiago",
#     "Talagante", "Tiltil", "Vitacura"
# ]

# def normalize_text(text: str) -> str:
#     text = (text or "").strip()
#     text = re.sub(r"\s+", " ", text)
#     return text

# def extract_local_and_comuna(header_tail: str):
#     text = normalize_text(header_tail)
#     if not text:
#         return "", ""

#     lower_text = text.lower()
#     matched = ""
#     best_pos = -1

#     for comuna in sorted(KNOWN_COMMUNAS, key=len, reverse=True):
#         pos = lower_text.rfind(comuna.lower())
#         if pos != -1 and pos > best_pos:
#             best_pos = pos
#             matched = comuna

#     if matched:
#         local = text[:best_pos].strip(" -")
#         comuna = text[best_pos:].strip(" -")
#         return local, comuna

#     parts = text.split()
#     if len(parts) >= 2:
#         return " ".join(parts[:-1]), parts[-1]

#     return text, ""

import re

KNOWN_COMMUNAS = [
    "Alhué", "Buin", "Calera de Tango", "Cerrillos", "Cerro Navia", "Colina",
    "Conchalí", "Curacaví", "El Bosque", "El Monte", "Estación Central",
    "Huechuraba", "Independencia", "Isla de Maipo", "La Cisterna", "La Florida",
    "La Granja", "La Pintana", "La Reina", "Lampa", "Las Condes", "Lo Barnechea",
    "Lo Espejo", "Lo Prado", "Macul", "Maipú", "María Pinto", "Melipilla",
    "Ñuñoa", "Padre Hurtado", "Paine", "Pedro Aguirre Cerda", "Peñaflor",
    "Peñalolén", "Pirque", "Providencia", "Pudahuel", "Puente Alto", "Quilicura",
    "Quinta Normal", "Recoleta", "Renca", "San Bernardo", "San Joaquín",
    "San José de Maipo", "San Miguel", "San Pedro", "San Ramón", "Santiago",
    "Talagante", "Tiltil", "Vitacura"
]


def normalize_text(text: str) -> str:
    text = (text or "").strip()
    text = re.sub(r"\s+", " ", text)
    return text


def extract_local_and_comuna(header_tail: str):
    text = normalize_text(header_tail)
    if not text:
        return "", ""

    lower_text = text.lower()
    matched = ""
    best_pos = -1

    for comuna in sorted(KNOWN_COMMUNAS, key=len, reverse=True):
        pos = lower_text.rfind(comuna.lower())
        if pos != -1 and pos > best_pos:
            best_pos = pos
            matched = comuna

    if matched:
        local = text[:best_pos].strip(" -")
        comuna = text[best_pos:].strip(" -")
        return local, comuna

    parts = text.split()
    if len(parts) >= 2:
        return " ".join(parts[:-1]), parts[-1]

    return text, ""