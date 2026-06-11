#!/usr/bin/env python3
from lib.generate_log import generate_log, fetch_data


if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
