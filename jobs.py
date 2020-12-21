"""
File that handles all the API calls to the different job board sites
---------------------------------------------------------------------
Author:K.*
re-worked 12/21/20
"""

import requests
import pathlib
import json
from xml.etree import ElementTree
from typing import Dict, List

# Global file location for read/write
path = pathlib.Path.cwd() / 'Available_Jobs.txt'


def pull_stackoverflow_data(stackoverflow_url) -> List[Dict]:
    print("\nStack Overflow:\n---------------")

    data = []

    for i in range(1, 127):
        print("Fetching page %s..." % (str(i)))
        response = requests.get(stackoverflow_url + "?sort=i&pg=" + str(i))
        root = ElementTree.fromstring(response.content)
        channel = root[0]

        print("Parsing XML...")
        for item in channel.iter('item'):
            company = item[2][0].text
            link = item.find('link').text
            title = item.find('title').text
            location = item[-1].text
            description = item.find('description').text

            raw_category = item.find('category')
            if raw_category is not None:
                category = raw_category.text
            else:
                category = "None"

            item_data = {"title": title, "company": company, "description": description, "url": link,
                         "category": category, "location": location}

            data.append(item_data)

    return data

def pull_partial_stackoverflow_data(stackoverflow_url) -> List[Dict]:
    print("\nStack Overflow:\n---------------")

    data = []

    print("Fetching page...")
    response = requests.get(stackoverflow_url)
    root = ElementTree.fromstring(response.content)
    channel = root[0]

    print("Parsing XML...")
    for item in channel.iter('item'):
        company = item[2][0].text
        link = item.find('link').text
        title = item.find('title').text
        description = item.find('description').text
        created = item.find('pubDate').text

        # retrieve info between last set of parens in title
        location = title[title.rfind("(") + 1:title.rfind(")")]

        # category data massaging
        raw_category = item.find('category')
        if raw_category is not None:
            category = raw_category.text
        else:
            category = "None"

        item_data = {"title": title, "company": company, "description": description, "url": link,
                     "category": category, "location": location, "created_at": created}
        data.append(item_data)

    return data