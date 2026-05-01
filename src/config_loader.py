import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CONFIG_DIR = BASE_DIR / "config"


def load_json(file_name: str):
    path = CONFIG_DIR / file_name
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_settings():
    return load_json("settings.json")


def load_keywords():
    return load_json("keywords.json")


def load_group_rules():
    return load_json("groups_rules.json")
