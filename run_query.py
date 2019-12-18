import requests
import json
import login

login.login()
headers = login.headers
domain = login.domain

query_id = input("Enter the query_id you wish to run: ")
format = input("Please specify one of the following formats: csv, json, json_detail, txt, html, md, xlsx, sql, png, jpeg: ")

run_query_url = f"https://{domain}:19999/api/3.1/queries/{query_id}/run/{format}"
query_results = requests.get(run_query_url, headers=headers)

print(query_results.content)
