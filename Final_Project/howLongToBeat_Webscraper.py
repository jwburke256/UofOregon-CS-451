"""
howLongToBeat.py: CS 451 Final Project
Author: Jacob Burke
Credit: GeeksforGeeks
This file scrapes ;
Date Modified: 05/27/2024
"""

import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import json
import time
from time import sleep
import random

# url with howLongToBeat backlog info
url = "https://howlongtobeat.com/user/WraithW0lf/games/backlog/1"


def create_session():
    session = requests.Session()
    retries = Retry(total=10, backoff_factor=0.2,
                    status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def scrape_howLongToBeat_data(session, url):
    # create empty list for links
    backlog_game_links = []

    # wait 5 seconds for request
    time.sleep(5)

    try:
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"}
        request = session.get(url=url, headers=headers)
        # request = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Connection error for {url}: {e}")
        return None

    print(request.status_code)
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, 'html5lib')
        print("test")
        print(request.content)


# create and close session
session = create_session()
get_jwst_data = scrape_howLongToBeat_data(session, url)
session.close()

# print done when finished
print("done")
