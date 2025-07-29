from dotenv import load_dotenv
import os
import ctypes  # Windows API calls
import time


# Load environment variables from .env file
load_dotenv()


# Prevent the system from sleeping
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001

interval = int(os.getenv("INTERVAL", 1))


print("Press Ctrl+C to stop the awaker.")
try:
    while True:
        # Continuously reset the execution state to prevent sleep
        ctypes.windll.kernel32.SetThreadExecutionState(
            ES_CONTINUOUS | ES_SYSTEM_REQUIRED
        )
        print("wakeup...")
        time.sleep(interval)  # Wait for x seconds
finally:
    # Restore normal behavior when the program exits
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
