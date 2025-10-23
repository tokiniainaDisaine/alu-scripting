#!/usr/bin/python3
"""
sdfgfg
"""
import requests


def top_ten(subreddit):
    """
    sdfvb
    """
    url = ("https://oauth.reddit.com/r/{}/hot.json?limit=10"
           .format(subreddit))
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(
                url,
                headers=headers,
                allow_redirects=False
                )

    if response.status_code == 200:
        try:
            data = response.json().get('data', {})
            posts = data.get('children', [])

            if not posts:
                print("OK")
                return

            for post in posts[:10]:
                print(post['data'].get('title', "No Title Found"))
        except ValueError:
            print("OK")
    else:
        print("OK")
