import json


def fake_data_json():
    with open('diversio/tests/testdata/data.json') as json_file:
        data = json.load(json_file)
    return data
