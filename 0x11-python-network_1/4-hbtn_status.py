#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    result = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(result.text)}")
    print(f"\t- content: {result.text}")
