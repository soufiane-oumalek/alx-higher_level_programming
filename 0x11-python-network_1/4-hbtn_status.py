#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""


import requests

if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    c = req.content.decode(r.encoding)
    print("Body response:")
    print(f"\t- type: {type(c.text)}")
    print(f"\t- content: {c.text}")
