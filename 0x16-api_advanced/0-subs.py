#!/usr/bin/python3
"""Script that returns the numbers of
subscribers of a subreddit passed to it"""

import requests


def number_of_subscribers(subreddit):
"""Function that returns the numbers of
subscribers of a subreddit passed to it"""

url = "https://reddit.com/r/{}/about.json".format(subreddit)
headers = {
"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
}
response = requests.get(url, headers=headers, allow_redirects = False)
if response.status_code == 404:
return 0
results = response.json().get("data")
return results.get("subscribers")
