#!/usr/bin/python3

"""
Query the API to return no of subscribers for a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    if invalid, function to give a 0
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
