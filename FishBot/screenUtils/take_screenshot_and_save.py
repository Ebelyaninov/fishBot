import os  # <-- Add this line
import mss
import mss.tools
from PIL import Image


def take_screenshot_and_save(filename="screenshot.png"):
    # Путь к папке для скриншотов
    # os.path.join() объединяет части пути, что делает его кроссплатформенным
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    # Полный путь к файлу
    filepath = os.path.join(screenshots_dir, filename)

    with mss.mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        img.save(filepath)

    print(f"Скриншот сохранен как {filepath}")


def get_screenshot_as_image():
    """
    Takes a screenshot and returns it as a Pillow Image object.
    """
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        return img