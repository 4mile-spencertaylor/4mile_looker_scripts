import requests
import json

# using basic inputs here, feel free to adapt to whatever process you impose to obtain the client id and secret 
# domain likely not necessary as variable, more for my testing purposes
domain = input("Enter Looker instance Domain (i.e. 4mile.looker.com): ")
client_id = input("Enter API Client ID: ")
client_secret = input("Enter API Client Secret: ")

# url allows us to obtain access_token specific to a user profile, necessary for all subsequent API calls
login_url = f"https://{domain}:19999/api/3.1/login?client_id={client_id}&client_secret={client_secret}"

# variable "headers" will be passed through all subsequent API calls
login_response = requests.post(login_url)
# if the following response is 200, it passed
print(login_response)
token = login_response.json()['access_token']
headers = {"Authorization": 'Bearer ' + token}

# more basic user input
space_id = input("Enter the Folder ID you wish to modify: ")
get_metadata_id_url = f"https://{domain}:19999/api/3.1/spaces/{space_id}"

metadata_id_response = requests.get(get_metadata_id_url, headers=headers)
metadata_id = metadata_id_response.json()['content_metadata_id']
# if the following response is 200, it passed
print(metadata_id_response)

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
print(create_metadata_access_response)
