#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import sys
import requests

if __name__ == "__main__":
    payload = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}

    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
