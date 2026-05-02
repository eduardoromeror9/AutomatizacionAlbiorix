# from datetime import datetime
# from pathlib import Path

# from src.config_loader import load_settings, load_keywords, load_group_rules
# from src.logger_setup import setup_logger
# from src.models import RunSummary
# from src.whatsapp.driver_factory import build_driver
# from src.whatsapp.sidebar_scanner import scan_sidebar_chats
# from src.whatsapp.chat_opener import open_chat_by_name
# from src.whatsapp.group_detector import is_probable_group
# from src.whatsapp.message_reader import read_visible_messages
# from src.parser.message_parser import parse_message_to_records
# from src.exporters.excel_exporter import export_records_to_excel
# from src.exporters.txt_log_exporter import export_run_summary_txt
# from src.utils.file_paths import resolve_output_dirs


# def run_app():
#     settings = load_settings()
#     keywords = load_keywords()
#     group_rules = load_group_rules()

#     output_dir, log_dir, profile_dir = resolve_output_dirs(settings)
#     logger, log_file = setup_logger(log_dir)
#     summary = RunSummary()
#     records = []

#     logger.info("Iniciando lector WhatsApp Albiorix")
#     logger.info("Perfil Chrome: %s", profile_dir)

#     driver = None
#     try:
#         driver = build_driver(settings, profile_dir)
#         chats = scan_sidebar_chats(driver, settings, logger)
#         summary.total_chats_seen = len(chats)
#         logger.info("Chats detectados: %s", len(chats))

#         max_chats = settings.get("max_chats_to_process", 100)
#         today = datetime.now().strftime("%d/%m/%Y")
#         execution_date = datetime.now().strftime("%Y-%m-%d")

#         for chat in chats[:max_chats]:
#             chat_name = chat.name.strip()
#             try:
#                 if settings.get("scan_only_groups", True):
#                     probable_group = chat.is_group or is_probable_group(chat_name)
#                     if not probable_group:
#                         logger.info("Omitido chat individual: %s", chat_name)
#                         continue

#                 open_chat_by_name(driver, chat_name, settings, logger)
#                 summary.processed_groups.append(chat_name)
#                 summary.total_groups_processed += 1

#                 messages = read_visible_messages(driver, chat_name, settings, logger)
#                 summary.total_messages_read += len(messages)

#                 for message in messages:
#                     parsed = parse_message_to_records(
#                         message=message,
#                         keywords_config=keywords,
#                         execution_date=execution_date,
#                         expected_date=today,
#                     )
#                     if parsed:
#                         records.extend(parsed)

#             except Exception as exc:
#                 error_msg = f"Error procesando chat '{chat_name}': {exc}"
#                 summary.errors.append(error_msg)
#                 logger.exception(error_msg)

#         summary.total_records = len(records)
#         summary.total_ambiguous = sum(1 for r in records if r.status != "OK")

#         excel_path = export_records_to_excel(records, output_dir)
#         txt_path = export_run_summary_txt(summary, records, log_dir, log_file)

#         logger.info("Excel generado: %s", excel_path)
#         logger.info("TXT generado: %s", txt_path)
#         logger.info("Proceso finalizado")

#     finally:
#         if driver:
#             driver.quit()


from datetime import datetime

from src.config_loader import load_settings, load_keywords, load_group_rules
from src.logger_setup import setup_logger
from src.models import RunSummary
from src.whatsapp.driver_factory import build_driver
from src.whatsapp.sidebar_scanner import scan_sidebar_chats
from src.whatsapp.chat_opener import open_chat_by_name
from src.whatsapp.group_detector import is_probable_group
from src.whatsapp.message_reader import read_visible_messages
from src.parser.message_parser import parse_message_to_records
from src.exporters.excel_exporter import export_records_to_excel
from src.exporters.txt_log_exporter import export_run_summary_txt
from src.utils.file_paths import resolve_output_dirs


def run_app():
    settings = load_settings()
    keywords = load_keywords()
    _ = load_group_rules()

    output_dir, log_dir, profile_dir = resolve_output_dirs(settings)
    logger, log_file = setup_logger(log_dir)
    summary = RunSummary()
    records = []

    logger.info("Iniciando lector WhatsApp Albiorix")
    logger.info("Modo demo: %s", settings.get("demo_mode", False))

    driver = None
    try:
        driver = build_driver(settings, profile_dir)

        today = datetime.now().strftime("%d/%m/%Y")
        execution_date = datetime.now().strftime("%Y-%m-%d")

        if settings.get("demo_mode", False):
            target_chat = settings.get("target_chat_name", "").strip()
            if not target_chat:
                raise ValueError("Debes configurar 'target_chat_name' en settings.json")

            logger.info("Abriendo chat demo: %s", target_chat)
            open_chat_by_name(driver, target_chat, settings, logger)

            summary.total_chats_seen = 1
            summary.total_groups_processed = 1
            summary.processed_groups.append(target_chat)

            messages = read_visible_messages(driver, target_chat, settings, logger)
            summary.total_messages_read = len(messages)

            for message in messages:
                parsed = parse_message_to_records(
                    message=message,
                    keywords_config=keywords,
                    execution_date=execution_date,
                    expected_date=today,
                )
                if parsed:
                    records.extend(parsed)

        else:
            chats = scan_sidebar_chats(driver, settings, logger)
            summary.total_chats_seen = len(chats)
            logger.info("Chats detectados: %s", len(chats))

            max_chats = settings.get("max_chats_to_process", 100)

            for chat in chats[:max_chats]:
                chat_name = chat.name.strip()
                try:
                    if settings.get("scan_only_groups", True):
                        probable_group = chat.is_group or is_probable_group(chat_name)
                        if not probable_group:
                            logger.info("Omitido chat individual: %s", chat_name)
                            continue

                    open_chat_by_name(driver, chat_name, settings, logger)
                    summary.processed_groups.append(chat_name)
                    summary.total_groups_processed += 1

                    messages = read_visible_messages(driver, chat_name, settings, logger)
                    summary.total_messages_read += len(messages)

                    for message in messages:
                        parsed = parse_message_to_records(
                            message=message,
                            keywords_config=keywords,
                            execution_date=execution_date,
                            expected_date=today,
                        )
                        if parsed:
                            records.extend(parsed)

                except Exception as exc:
                    error_msg = f"Error procesando chat '{chat_name}': {exc}"
                    summary.errors.append(error_msg)
                    logger.exception(error_msg)

        summary.total_records = len(records)
        summary.total_ambiguous = sum(1 for r in records if r.status != "OK")

        excel_path = export_records_to_excel(records, output_dir)
        txt_path = export_run_summary_txt(summary, records, log_dir, log_file)

        logger.info("Excel generado: %s", excel_path)
        logger.info("TXT generado: %s", txt_path)
        logger.info("Proceso finalizado")

    finally:
        if driver:
            driver.quit()