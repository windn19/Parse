import os


def clear_price(text):
    price = [char for char in text if char.isdigit()] if text else None
    return int(''.join(price)) if price else None


def clear_file(file):
    if os.path.exists(file):
        os.remove(file)
