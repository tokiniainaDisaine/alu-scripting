#!/usr/bin/python3
"""
sdfgfg
"""
import requests


def top_ten(subreddit):
    """
    sdfvb
    """
    url = "https://www.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}

    response = requests.get(
                url,
                headers=headers,
                allow_redirects=False
                )

    if response.status_code != 200:
        print(None)
        return
    posts = response.json()['data']['children']
    for post in posts:
        print(post['data']['title'])
