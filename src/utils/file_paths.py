from pathlib import Path


def resolve_output_dirs(settings: dict):
    base = Path(__file__).resolve().parents[2]

    output_dir = Path(settings.get("output_dir", ".\\data\\output"))
    log_dir = Path(settings.get("log_dir", ".\\data\\logs"))
    profile_dir = Path(settings.get("chrome_profile_dir", ".\\data\\chrome_profile"))

    if not output_dir.is_absolute():
        output_dir = base / output_dir
    if not log_dir.is_absolute():
        log_dir = base / log_dir
    if not profile_dir.is_absolute():
        profile_dir = base / profile_dir

    output_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)
    profile_dir.mkdir(parents=True, exist_ok=True)

    return str(output_dir), str(log_dir), str(profile_dir)
