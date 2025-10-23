#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    number_of_subscribers
    """
    url = f"https://oauth.reddit.com/r/{str(subreddit)}/about"
    headers = {"User-Agent": "Mozilla/5.0"}  

    response = requests.get(
                url, 
                headers=headers, 
                allow_redirects=False
                )

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
