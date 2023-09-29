#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        res = requests.get(url)
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
