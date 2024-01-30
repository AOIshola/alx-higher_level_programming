#!/usr/bin/python3
"""Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


import requests
import sys

if __name__ == "__main__":
#    headers = {"Authorization": "Bearer" sys.argv[2],\
 #           X-GitHub-Api-Version: "2022-11-28"}
  #  req = requests.get("https://api.github.com/octocat", headers = headers)

   # print(req.text)
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    headers = {
        "Authorization": "Basic " + (f"{username}:{token}").encode("ascii").b64encode().decode("utf-8"),
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_id = response.json()["id"]
        print(f"Your GitHub user ID is: {user_id}")
    else:
        print(f"Failed to retrieve user ID. Status code: {response.status_code}")
