import os
from PIL import Image

# Импортируем обе функции напрямую из пакета FishBot.screenUtils
from FishBot.screenUtils import take_screenshot_and_save, get_screenshot_as_image

def test_take_screenshot_and_save_creates_file():
    """Проверяет, что функция создает файл и его можно открыть."""
    filename = "test_screenshot.png"
    screenshots_dir = "screenshots" # <-- Добавляем путь к папке
    filepath = os.path.join(screenshots_dir, filename) # <-- Создаем полный путь

    # Вызываем функцию
    take_screenshot_and_save(filename)

    # Проверяем, что файл был создан по ПРАВИЛЬНОМУ пути
    assert os.path.exists(filepath)

    # Проверяем, что файл можно открыть как изображение
    try:
        Image.open(filepath)
        is_valid = True
    except IOError:
        is_valid = False

    assert is_valid

    # Удаляем тестовый файл по ПРАВИЛЬНОМУ пути
    os.remove(filepath)