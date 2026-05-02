from pathlib import Path
from datetime import datetime


def export_summary_txt(records, logs_dir: str, chat_name: str):
    Path(logs_dir).mkdir(parents=True, exist_ok=True)
    total = len(records)
    groups = sorted({r.group_name for r in records if r.group_name})
    ambiguous = [r for r in records if r.status != "OK"]

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = Path(logs_dir) / f"resumen_{stamp}.txt"

    lines = []
    lines.append("RESUMEN EJECUCION WHATSAPP ALBIORIX")
    lines.append("=" * 50)
    lines.append(f"Chats detectados: {len(groups) if groups else 1}")
    lines.append(f"Grupos procesados: {len(groups) if groups else 1}")
    lines.append(f"Mensajes leidos: {total}")
    lines.append(f"Registros generados: {total}")
    lines.append(f"Casos ambiguos: {len(ambiguous)}")
    lines.append("")
    lines.append("GRUPOS PROCESADOS")
    lines.append("-" * 50)
    for g in groups or [chat_name]:
        lines.append(f"- {g}")
    lines.append("")
    lines.append("ERRORES")
    lines.append("-" * 50)
    if ambiguous:
        for r in ambiguous:
            lines.append(f"- {r.message_date} {r.message_time} {r.notes}")
    else:
        lines.append("- Sin errores registrados")
    lines.append("")
    lines.append("ESTADOS DISTINTOS DE OK")
    lines.append("-" * 50)
    if ambiguous:
        for r in ambiguous:
            lines.append(f"- {r.status}: {r.notes}")
    else:
        lines.append("- No hay casos ambiguos")

    path.write_text("\n".join(lines), encoding="utf-8")
    return str(path)