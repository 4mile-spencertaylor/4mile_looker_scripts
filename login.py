# test commit message
import os
import requests
import json
import sys

domain = "4mile.looker.com"
client_id = os.getenv('LOOKER_CLIENT_ID')
client_secret = os.getenv('LOOKER_CLIENT_SECRET')


def login():
    breakpoint()
    login_url = f"https://{domain}:19999/api/3.1/login?client_id={client_id}&client_secret={client_secret}"
    login_response = requests.post(login_url)
    token = login_response.json()['access_token']
    os.environ['headers'] = str({"Authorization": 'Bearer ' + token})

    if "200" in str(login_response):
        print("Login successful")
    else:
        print("Login unsuccessful")
        print(login_response.content)
        sys.exit()

# login()

def sudo_login():
    user_id = input("Enter the user_id for whom you wish to obtain an access_token: ")
    user_login_url = f"https://{domain}:19999/api/3.1/login?user_id={user_id}&client_id={client_id}&client_secret={client_secret}"
    user_login_response = requests.post(user_login_url)
    token = user_login_response.json()['access_token']
    os.environ['headers'] = str({"Authorization": 'Bearer ' + token})

    if "200" in str(user_login_response):
        print(f"Login as user {user_id} successful")
    else:
        print("Login unsuccessful")
        print(user_login_response.content)
        sys.exit()
