import json
import requests

def get(url):
    try:
        response = requests.get(url=url)
        if response.status_code != 200:
            raise
    except requests.exceptions.RequestException as e:
        print("{0} {1}".format(title or '' , msg))

    response.raise_for_status()
    value = response.json()

    return response, value
