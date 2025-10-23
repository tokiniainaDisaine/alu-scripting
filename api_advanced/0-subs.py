#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    number_of_subscribers
    """
    url = "https://www.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}  

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
