from . import screenUtils

# Now you access the functions using dot notation from the screenUtils module
screenUtils.take_screenshot_and_save("my_new_screenshot.png")

# Get the screenshot as an image object
screenshot_image = screenUtils.get_screenshot_as_image()

# Print the image size
print(f"Размер скриншота: {screenshot_image.size}")