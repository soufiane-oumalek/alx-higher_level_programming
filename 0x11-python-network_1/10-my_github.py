#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username, password = sys.argv[1], sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    response = requests.get("https://api.github.com/user", auth=auth)
    user_data = response.json()
    user_id = user_data.get("id")
    print(user_id)
