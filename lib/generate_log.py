#!/usr/bin/env python3
from datetime import datetime


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    filename = f"log_{datetime.now():%Y%m%d}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data():
    try:
        import requests
    except ImportError:
        return {}

    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return {}


if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
