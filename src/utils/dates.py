from datetime import datetime


def today_display():
    return datetime.now().strftime("%d/%m/%Y")
