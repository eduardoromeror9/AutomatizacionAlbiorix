import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_chat_by_name(driver, chat_name, settings, logger):
    wait = WebDriverWait(driver, settings.get("wait_seconds", 20))
    boxes = driver.find_elements(By.XPATH, '//div[@contenteditable="true"][@role="textbox"]')
    if not boxes:
        raise RuntimeError("No se encontró caja de búsqueda")

    box = boxes[0]
    box.click()
    box.send_keys(Keys.CONTROL, 'a')
    box.send_keys(Keys.DELETE)
    box.send_keys(chat_name)
    time.sleep(1.2)

    target = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{chat_name}"]')))
    target.click()
    time.sleep(float(settings.get("chat_open_pause_seconds", 2.0)))
    logger.info("Chat abierto: %s", chat_name)
