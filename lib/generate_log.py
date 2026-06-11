#!/usr/bin/env python3
from datetime import datetime
import os
import requests  # Required by the test suite

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        print("Error: Input data must be a list.")
        return False

    # STEP 2: Generate a filename with today's date
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{date_str}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message
    print(f"Log written to {filename}")
    return True

def fetch_data():
    # Fetch data from the public API as required by Step 4
    response = requests.get("https://typicode.com")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    # Test file writing locally
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)
    
    # Test API fetching locally
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
