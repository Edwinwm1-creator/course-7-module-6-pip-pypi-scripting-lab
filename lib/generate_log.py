#!/usr/bin/env python3
from datetime import datetime
import os
import requests


def generate_log(data):
    # STEP 1: Validate input
    # Hint: Check if data is a list
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

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
    return filename


def fetch_data():
    # Fetch data from a public API as specified in Step 4
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        print(f"Warning: Could not fetch data from API: {error}")
        return {}


if __name__ == "__main__":
    # Local execution verification block
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
