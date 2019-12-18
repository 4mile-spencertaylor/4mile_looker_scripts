import requests
import json
import login
import os

login.sudo_login()
domain = login.domain
headers = {}
headers = os.getenv('headers')


get_dashboards_url = f"https://{domain}:19999/api/3.1/dashboards"
dashboards_response = requests.get(get_dashboards_url, headers = headers)

# dahsboards = []
# dashboards = [item['title'] for item in dashboards_response.json()]
#
# with open('dashboards.json', 'w') as f:
#     json.dump(dashboards, f)
