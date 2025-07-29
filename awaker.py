from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

import pyautogui
import time


interval = int(os.getenv("INTERVAL", 1))

while True:
    pyautogui.move(1, 0)  # Move mouse one pixel to the right
    pyautogui.move(-1, 0)  # Move mouse back to the left
    time.sleep(interval)  # Wait for x seconds
