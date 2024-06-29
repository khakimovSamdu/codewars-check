import requests
username = 'SoliyevNurbek'
# url = f'https://www.codewars.com/api/v1/users/{username}/'
# get = requests.get(url=url)
# problem = '545a4c5a61aa4c6916000755'
# url_train = f'https://www.codewars.com/kata/{problem}'
# get_data = requests.get(url=url_train)
page = 0
url_comp = f'https://www.codewars.com/api/v1/users/{username}/code-challenges/completed'
get_problems = requests.get(url=url_comp).json()
print(get_problems)
# url = f'https://www.codewars.com/api/v1/users/{username}/code-challenges/authored'
# get = requests.get(url=url).json()
# print(get)
# challenge = 'the-wide-mouthed-frog'
# url2 = f'https://www.codewars.com/api/v1/code-challenges/{challenge}'