# This script will add all groups in the Looker instance to a single group, hardcoded below

import login
import requests
import json

from http import HTTPStatus

headers = login.login() # log in to the API, return the header needed for subsequent API calls (access_token)
domain = login.domain

# Get all group id's
get_groups_url = f"https://{domain}:19999/api/3.1/groups"
groups_response = requests.get(get_groups_url, headers=headers)

if groups_response.status_code == HTTPStatus.OK:
    groups_content = groups_response.content
    res_dict = json.loads(groups_content.decode('utf-8')) # results coming back as bytes, so need to convert to list

    ids = [item['id'] for item in res_dict]

else:
    print("Unable to make request. Please check credentials and network connectivity.")
    quit()

super_group_id = "2714" # need to change this to ufa's super group
for id in ids:
    add_group_url = f"https://{domain}:19999/api/3.1/groups/{super_group_id}/groups"
    body = {"group_id":id}
    add_groups_response = requests.post(add_group_url, headers=headers, json=body)

    print(add_groups_response)
