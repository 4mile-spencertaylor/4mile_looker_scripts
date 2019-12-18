import requests
import json
import login
import sys

login.login()
headers = login.headers
domain = login.domain

# more basic user input
space_id = input("Enter the Folder ID you wish to modify: ")
get_metadata_id_url = f"https://{domain}:19999/api/3.1/spaces/{space_id}"

metadata_id_response = requests.get(get_metadata_id_url, headers=headers)
metadata_id = metadata_id_response.json()['content_metadata_id']
# if the following response is 200, it passed
if "200" in metadata_id_response:
    print("")
else:
    print("Failed")
    print(metadata_id_response.content)
    sys.exit()

# more basic user input
user_id = input("Enter user ID to add to folder: ")
permission_type = input("Enter view or edit for the permission type this user should have on this folder: ")

folder_permission_data = {
  "content_metadata_id": str(metadata_id),
  "permission_type": permission_type,
  "user_id": user_id
}

create_metadata_access_url = f"https://{domain}:19999/api/3.1/content_metadata_access"
create_metadata_access_response = requests.post(create_metadata_access_url, json=folder_permission_data, headers=headers)
# if the following response is 200, it passed. If not, it's possible the user already has access to the folder

if "200" in str(create_metadata_access_response):
    print("Success!")
else:
    print("Failed")
    print(create_metadata_access_response.content)
