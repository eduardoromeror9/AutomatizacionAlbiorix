SIDEBAR_CHAT_ITEMS = [
    '//div[@id="pane-side"]//div[@role="listitem"]',
    '//div[@id="pane-side"]//div[contains(@class,"_ak72")]',
]

SEARCH_BOX = [
    '//div[@contenteditable="true"][@data-tab="3"]',
    '//div[@contenteditable="true"][@role="textbox"]',
]

CHAT_HEADER = [
    '//header',
]

MESSAGE_BLOCKS = [
    '//div[contains(@data-pre-plain-text, "[")]',
    '//div[contains(@class,"message-") or @data-pre-plain-text]',
]
