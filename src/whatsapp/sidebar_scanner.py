import time
from selenium.webdriver.common.by import By


def scan_sidebar_chats(driver, settings, logger):
    pause = float(settings.get("sidebar_pause_seconds", 1.2))
    max_scrolls = int(settings.get("max_sidebar_scrolls", 50))
    pane = driver.find_element(By.ID, "pane-side")

    seen = {}

    for i in range(max_scrolls):
        items = pane.find_elements(By.XPATH, './/div[@role="listitem"]')
        for item in items:
            text = item.text.strip().split("\n")[0].strip()
            if text:
                seen[text] = text

        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", pane)
        time.sleep(pause)
        logger.info("Scroll sidebar %s/%s | chats acumulados: %s", i + 1, max_scrolls, len(seen))

    chats = []
    from src.models import ChatItem
    for name in seen.keys():
        chats.append(ChatItem(name=name, is_group=True, raw_title=name))
    return chats
