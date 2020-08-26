# import keyword
#
#
# def contains_keyword(*args):
#     for item in args:
#         if keyword.iskeyword(item):
#             return True
#     return False
# -----------------------------------------------------------------------------------------------

import requests

# # url get request and response status. 200 is successful.
# url = "https://www.linkedin.com/feed/"
# response = requests.get(url)
# print(f"Your request to {url} came back with status code {response.status_code}")
# ----------------------------------------------------------------------------------------------

# url = "https://icanhazdadjoke.com/"
#
# # get request to url, save in variable. Get the json version from the api.
# response = requests.get(url, headers={"Accept": "application/json"})
#
# # Converts the json from website to python code and turned into a dictionary.
# data = response.json()
#
# # print the json saved in the variable and only the value from the key, joke.
# print(data["joke"])
# ----------------------------------------------------------------------------------------------

url = "https://icanhazdadjoke.com//search"

# get request to url, save in variable. Get the json version from the api.
# From parameters, return 1 joke that is related to search term, cat.
response = requests.get(url, headers={"Accept": "application/json"}, params={"term": "cat", "limit": 1})

# Converts the json from website to python code and turned into a dictionary.
data = response.json()

# print the json saved in the variable and only the value from the key, results.
print(data["results"])

