from datetime import datetime
from pathlib import Path


def export_run_summary_txt(summary, records, log_dir: str, log_file: str):
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = Path(log_dir) / f"resumen_{stamp}.txt"

    with open(path, "w", encoding="utf-8") as f:
        f.write("RESUMEN EJECUCION WHATSAPP ALBIORIX\n")
        f.write("=" * 50 + "\n")
        f.write(f"Chats detectados: {summary.total_chats_seen}\n")
        f.write(f"Grupos procesados: {summary.total_groups_processed}\n")
        f.write(f"Mensajes leidos: {summary.total_messages_read}\n")
        f.write(f"Registros generados: {summary.total_records}\n")
        f.write(f"Casos ambiguos: {summary.total_ambiguous}\n")
        f.write(f"Log tecnico: {log_file}\n\n")

        f.write("GRUPOS PROCESADOS\n")
        f.write("-" * 50 + "\n")
        for group in summary.processed_groups:
            f.write(f"- {group}\n")

        f.write("\nERRORES\n")
        f.write("-" * 50 + "\n")
        if summary.errors:
            for err in summary.errors:
                f.write(f"- {err}\n")
        else:
            f.write("- Sin errores registrados\n")

        f.write("\nESTADOS DISTINTOS DE OK\n")
        f.write("-" * 50 + "\n")
        non_ok = [r for r in records if r.status != "OK"]
        if non_ok:
            for r in non_ok[:300]:
                f.write(f"[{r.group_name}] {r.status} | {r.variant} | {r.message_text[:180]}\n")
        else:
            f.write("- No hay casos ambiguos\n")

    return str(path)
