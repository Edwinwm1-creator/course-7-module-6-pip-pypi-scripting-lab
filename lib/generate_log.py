#!/usr/bin/env python3
from datetime import datetime
import os

def generate_log(data):
    # STEP 1: Validate input
    # Hint: Check if data is a list
    if not isinstance(data, list):
        print("Error: Input data must be a list.")
        return False

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{date_str}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")
    return True

if __name__ == "__main__":
    # Example execution block to test locally
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)
