from src.parser.normalizer import normalize_text


def find_keyword_variants(text: str, keywords_config: dict):
    normalized = normalize_text(text)
    found = []
    for category, variants in keywords_config.items():
        for variant in variants:
            normalized_variant = normalize_text(variant)
            if normalized_variant in normalized:
                found.append((category, variant))
    return found
