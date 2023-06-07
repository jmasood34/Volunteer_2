import requests


def daily_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        quote = data ['content']
        author = data ['author']
        return quote,author


    else:
        return None