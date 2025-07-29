from dotenv import load_dotenv
import os
import keyboard  # For simulating key presses
import time


# Load environment variables from .env file
load_dotenv()


interval = int(os.getenv("INTERVAL", 1))


print("Press Ctrl+C to stop the awaker.")
try:
    while True:
        # Simulate a key press to keep the system awake
        keyboard.press_and_release("shift")  # Press and release the Shift key
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        print(f"{timestamp} wakeup...")
        time.sleep(interval)  # Wait for x seconds
except KeyboardInterrupt:
    print("\nAwaker interrupted by user. Exiting...")
finally:
    print("Awaker stopped.")
