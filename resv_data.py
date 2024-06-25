import requests
username = 'SoliyevNurbek'
url = f'https://www.codewars.com/api/v1/users/{username}/'
get = requests.get(url=url)
print(get.json())