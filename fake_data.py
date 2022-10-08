import json
import os

def fake_data_json():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return data