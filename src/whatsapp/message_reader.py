import re
from selenium.webdriver.common.by import By
from src.models import MessageItem


def read_visible_messages(driver, chat_name, settings, logger):
    blocks = driver.find_elements(By.XPATH, '//div[@data-pre-plain-text]')
    messages = []
    for block in blocks[-settings.get("max_messages_per_chat", 250):]:
        meta = block.get_attribute("data-pre-plain-text") or ""
        text = block.text.strip()
        sender = ""
        date = ""
        time = ""

        m = re.search(r'\[(\d{1,2}:\d{2}),\s(\d{1,2}/\d{1,2}/\d{2,4})\]\s([^:]+):', meta)
        if m:
            time = m.group(1)
            date = m.group(2)
            sender = m.group(3).strip()

        if text:
            messages.append(MessageItem(
                chat_name=chat_name,
                message_text=text,
                sender=sender,
                message_date=date,
                message_time=time,
                raw_meta=meta,
            ))

    logger.info("Mensajes visibles leídos en %s: %s", chat_name, len(messages))
    return messages
