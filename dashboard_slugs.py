#  purpose: get all dashboard slugs based on corresponding id's

# to run this script:
#   1. Download and install python3+ if you haven't already: https://www.python.org/downloads/
#   2. Open the terminal and change the directory to the pathway in which this file is stored
#   3. Type 'python3 dashboard_slugs.py'
#   4. Hit enter and follow the prompts
#       4a. To obtain your client ID and secret, edit your user credentials within the Looker UI
#           and view/edit your API keys

import requests
import json
import login
import sys


login.login()
headers = login.headers
domain = login.domain

get_dashboards_url = "https://" + domain + ":19999/api/3.1/dashboards"
slug_base_url = "https://" + domain + ":19999/api/3.1/dashboards/search?id="
dashboards = requests.get(get_dashboards_url, headers=headers)

# get list of dashboard ids
ids = []
ids = [item['id'] for item in dashboards.json()]

# loop through all ids and return slug
slugs = {}
for id in ids:
    slug_url = slug_base_url + str(id)
    slug_response = requests.get(slug_url, headers=headers)
    for slug in slug_response.json():
        slugs[id] = slug['slug']


# dump json
with open('slugs.json', 'w') as f:
    json.dump(slugs, f)
