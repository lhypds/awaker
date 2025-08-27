from dotenv import load_dotenv
import os
import keyboard  # For simulating key presses
import time


# Load environment variables from .env file
load_dotenv()


interval = int(os.getenv("INTERVAL", 1))
key = os.getenv("KEY", "shift")  # shift is the default key
print(f"INTERVAL: {interval} seconds")
print(f"KEY: {key}")


print("Press Ctrl+C to stop the awaker.")
try:
    while True:
        # Simulate a key press to keep the system awake
        keyboard.press_and_release(key)  # Press and release the specified key
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        print(f"\rwakeup - {timestamp}...", end="", flush=True)
        time.sleep(interval)  # Wait for x seconds
except KeyboardInterrupt:
    print("\nAwaker interrupted by user. Exiting...")
finally:
    print("Awaker stopped.")
