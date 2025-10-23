#!/usr/bin/python3
"""
sdfgfg
"""
import requests


def top_ten(subreddit):
    """
    sdfvb
    """
    url = "https://oauth.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}

    response = requests.get(
                url,
                headers=headers,
                allow_redirects=False
                )

    if response.status_code != 200:
        print(None)
        return
    else:
        posts = response.json()["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
