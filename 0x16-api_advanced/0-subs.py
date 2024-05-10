#!/usr/bin/python3
""" How many subs? """


import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}  # Set a custom User-Agent header

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
    except requests.exceptions.RequestException:
        pass

    return 0  # Return 0 if an error occurs or the subreddit is invalid
