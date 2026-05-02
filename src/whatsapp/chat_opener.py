# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# def open_chat_by_name(driver, chat_name, settings, logger):
#     wait = WebDriverWait(driver, settings.get("wait_seconds", 20))
#     boxes = driver.find_elements(By.XPATH, '//div[@contenteditable="true"][@role="textbox"]')
#     if not boxes:
#         raise RuntimeError("No se encontró caja de búsqueda")

#     box = boxes[0]
#     box.click()
#     box.send_keys(Keys.CONTROL, 'a')
#     box.send_keys(Keys.DELETE)
#     box.send_keys(chat_name)
#     time.sleep(1.2)

#     target = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{chat_name}"]')))
#     target.click()
#     time.sleep(float(settings.get("chat_open_pause_seconds", 2.0)))
#     logger.info("Chat abierto: %s", chat_name)


# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# def open_chat_by_name(driver, chat_name, settings, logger):
#     wait = WebDriverWait(driver, settings.get("wait_seconds", 20))

#     search_box = wait.until(
#         EC.presence_of_element_located(
#             (By.XPATH, '//div[@contenteditable="true"][@role="textbox"]')
#         )
#     )

#     search_box.click()
#     time.sleep(0.5)
#     search_box.send_keys(Keys.CONTROL, "a")
#     search_box.send_keys(Keys.DELETE)
#     search_box.send_keys(chat_name)
#     time.sleep(1.5)

#     target = wait.until(
#         EC.element_to_be_clickable(
#             (By.XPATH, f'//span[@title="{chat_name}"]')
#         )
#     )
#     target.click()

#     time.sleep(float(settings.get("chat_open_pause_seconds", 2.0)))
#     logger.info("Chat abierto correctamente: %s", chat_name)


# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException


# SEARCH_BOX_CANDIDATES = [
#     '//div[@id="side"]//div[@contenteditable="true"][@data-tab="3"]',
#     '//div[@id="side"]//div[@contenteditable="true"][@role="textbox"]',
#     '//div[@contenteditable="true"][@data-tab="3"]',
#     '//div[@contenteditable="true"][@role="textbox"]'
# ]

# CHAT_RESULT_CANDIDATES = [
#     '//span[@title="{name}"]',
#     '//div[@id="pane-side"]//span[@title="{name}"]'
# ]


# def _find_first_visible(driver, wait, xpaths):
#     last_error = None
#     for xpath in xpaths:
#         try:
#             element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
#             return element, xpath
#         except Exception as exc:
#             last_error = exc
#     if last_error:
#         raise last_error
#     raise RuntimeError("No se encontró elemento visible con los selectores dados")


# def open_chat_by_name(driver, chat_name, settings, logger):
#     wait_seconds = int(settings.get("wait_seconds", 30))
#     wait = WebDriverWait(driver, wait_seconds)

#     logger.info("Esperando carga de panel lateral...")
#     wait.until(EC.presence_of_element_located((By.ID, "pane-side")))

#     logger.info("Buscando caja de búsqueda...")
#     search_box, used_xpath = _find_first_visible(driver, wait, SEARCH_BOX_CANDIDATES)
#     logger.info("Caja de búsqueda encontrada con selector: %s", used_xpath)

#     search_box.click()
#     time.sleep(0.5)
#     search_box.send_keys(Keys.CONTROL, "a")
#     search_box.send_keys(Keys.DELETE)
#     time.sleep(0.3)
#     search_box.send_keys(chat_name)
#     time.sleep(2.0)

#     for pattern in CHAT_RESULT_CANDIDATES:
#         xpath = pattern.format(name=chat_name)
#         try:
#             logger.info("Intentando abrir chat con selector: %s", xpath)
#             target = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
#             target.click()
#             time.sleep(float(settings.get("chat_open_pause_seconds", 2.0)))
#             logger.info("Chat abierto correctamente: %s", chat_name)
#             return
#         except TimeoutException:
#             continue

#     logger.warning("No se encontró chat clickeable por title exacto. Intentando ENTER sobre búsqueda.")
#     search_box.send_keys(Keys.ENTER)
#     time.sleep(float(settings.get("chat_open_pause_seconds", 2.0)))

#     try:
#         header = wait.until(EC.presence_of_element_located((By.XPATH, '//header')))
#         logger.info("Chat abierto por ENTER: %s", chat_name)
#         return
#     except TimeoutException:
#         raise TimeoutException(f"No fue posible abrir el chat objetivo: {chat_name}")


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


SEARCH_BOX_CANDIDATES = [
    '//div[@id="side"]//div[@title="Search input textbox"]',
    '//div[@id="side"]//div[@contenteditable="true"][@data-tab="3"]',
    '//div[@id="side"]//div[@contenteditable="true"][@role="textbox"]',
    '//div[@title="Search input textbox"]',
    '//div[@contenteditable="true"][@data-tab="3"]',
    '//div[@contenteditable="true"][@role="textbox"]',
]


def _find_search_box(driver, wait, logger):
    last_error = None
    for xpath in SEARCH_BOX_CANDIDATES:
        try:
            logger.info("Probando selector buscador: %s", xpath)
            el = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return el, xpath
        except Exception as exc:
            last_error = exc
    raise TimeoutException(f"No se encontró la caja de búsqueda. Último error: {last_error}")


def open_chat_by_name(driver, chat_name, settings, logger):
    wait_seconds = int(settings.get("wait_seconds", 30))
    wait = WebDriverWait(driver, wait_seconds)

    logger.info("Esperando carga de panel lateral...")
    wait.until(EC.presence_of_element_located((By.ID, "pane-side")))

    logger.info("Buscando caja de búsqueda...")
    search_box, used_xpath = _find_search_box(driver, wait, logger)
    logger.info("Caja de búsqueda encontrada con selector: %s", used_xpath)

    search_box.click()
    time.sleep(0.5)
    search_box.send_keys(Keys.CONTROL, "a")
    search_box.send_keys(Keys.DELETE)
    time.sleep(0.3)
    search_box.send_keys(chat_name)
    time.sleep(2.0)

    result_xpaths = [
        f'//span[@title="{chat_name}"]',
        f'//div[@id="pane-side"]//span[@title="{chat_name}"]',
        f'//span[contains(@title, "{chat_name}")]'
    ]

    for xpath in result_xpaths:
        try:
            logger.info("Intentando abrir chat con selector: %s", xpath)
            target = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            target.click()
            time.sleep(float(settings.get("chat_open_pause_seconds", 2.0)))
            logger.info("Chat abierto correctamente: %s", chat_name)
            return
        except TimeoutException:
            continue

    logger.warning("No se encontró chat clickeable por title exacto. Intentando ENTER sobre búsqueda.")
    search_box.send_keys(Keys.ENTER)
    time.sleep(float(settings.get("chat_open_pause_seconds", 2.0)))

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, '//header')))
        logger.info("Chat abierto por ENTER: %s", chat_name)
        return
    except TimeoutException:
        raise TimeoutException(f"No fue posible abrir el chat objetivo: {chat_name}")