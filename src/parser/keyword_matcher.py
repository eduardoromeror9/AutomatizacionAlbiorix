# from src.parser.normalizer import normalize_text


# def find_keyword_variants(text: str, keywords_config: dict):
#     normalized = normalize_text(text)
#     found = []
#     for category, variants in keywords_config.items():
#         for variant in variants:
#             normalized_variant = normalize_text(variant)
#             if normalized_variant in normalized:
#                 found.append((category, variant))
#     return found


# import re
# from src.parser.normalizer import normalize_text


# def find_best_keyword_match(text: str, keywords_config: dict):
#     normalized = normalize_text(text)
#     matches = []

#     for category, variants in keywords_config.items():
#         ordered_variants = sorted(variants, key=len, reverse=True)

#         for variant in ordered_variants:
#             normalized_variant = normalize_text(variant)
#             pattern = r'(?<!\w)' + re.escape(normalized_variant) + r'(?!\w)'
#             if re.search(pattern, normalized):
#                 matches.append((category, variant, len(normalized_variant)))

#     if not matches:
#         return None

#     matches.sort(key=lambda x: x[2], reverse=True)
#     return matches[0][0], matches[0][1]

# import re
# from src.parser.normalizer import normalize_text


# def find_best_keyword_match(text: str, keywords_config: dict):
#     normalized = normalize_text(text)
#     matches = []
#     for category, variants in keywords_config.items():
#         for variant in sorted(variants, key=len, reverse=True):
#             nv = normalize_text(variant)
#             pattern = r'(?<!\w)' + re.escape(nv) + r'(?!\w)'
#             if re.search(pattern, normalized):
#                 matches.append((category, variant, len(nv)))
#     if not matches:
#         return None
#     matches.sort(key=lambda x: x[2], reverse=True)
#     return matches[0][0], matches[0][1]

# import re
# from src.parser.normalizer import normalize_text

# def find_best_keyword_match(text: str, keywords_config: dict):
#     normalized = normalize_text(text)
#     matches = []
#     for category, variants in keywords_config.items():
#         for variant in sorted(variants, key=len, reverse=True):
#             nv = normalize_text(variant)
#             pattern = r'(?<!\w)' + re.escape(nv) + r'(?!\w)'
#             if re.search(pattern, normalized):
#                 matches.append((category, variant, len(nv)))
#     if not matches:
#         return None
#     matches.sort(key=lambda x: x[2], reverse=True)
#     return matches[0][0], matches[0][1]

import re
from src.parser.normalizer import normalize_text

def find_best_keyword_match(text: str, keywords_config: dict):
    normalized = normalize_text(text)
    matches = []
    for category, variants in keywords_config.items():
        for variant in sorted(variants, key=len, reverse=True):
            nv = normalize_text(variant)
            pattern = r'(?<!\w)' + re.escape(nv) + r'(?!\w)'
            if re.search(pattern, normalized):
                matches.append((category, variant, len(nv)))
    if not matches:
        return None
    matches.sort(key=lambda x: x[2], reverse=True)
    return matches[0][0], matches[0][1]