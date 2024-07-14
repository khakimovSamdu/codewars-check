import requests
from datetime import datetime


def daily(user) -> int:
    URL = f'https://www.codewars.com/api/v1/users/{user}/code-challenges/completed'
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        count = 0
        for CompletedChallenge in data['data']:
            date = datetime.fromisoformat(CompletedChallenge['completedAt'])
            now = datetime.now()
            day, month, year = date.day,  date.month, date.year
            day_now, month_now, year_now = now.day-1, now.month, now.year
            if day==day_now and month==month_now and year==year_now:
                count += 1
                print(CompletedChallenge)

        return count
    
    else:
        return 0

print(daily('allamurodxakimov'))