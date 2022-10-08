import json
import requests
import datetime
from utils import _dict, median


def get(url):
    try:
        response = requests.get(url=url)
        if response.status_code != 200:
            raise
    except requests.exceptions.RequestException as e:
        print("{0} {1}".format(title or '', msg))

    response.raise_for_status()
    return response.json()


def output(response):
    monitor = _dict(_dict(response).monitor)
    sorted_response_times = sorted(
        monitor.responseTimes, key=lambda x: x["value"], reverse=True)
    highest = sorted_response_times[0]
    lowest = sorted_response_times[-1]
    median_time = median(sorted_response_times)

    strptime_format = "%B %d, %Y, %H:%M"
    timezone = datetime.timezone(datetime.timedelta(hours=6))

    current_time = datetime.datetime.now(datetime.timezone.utc)
    print(current_time)
    print(current_time.timestamp())
    highest_datetime = datetime.datetime.strptime(
        highest["datetime"], strptime_format).replace(
        tzinfo=timezone)
    print(highest_datetime)
    print(highest_datetime.timestamp())
    highest_in_last_days = (
        current_time - highest_datetime).days
    lowest_datetime = datetime.datetime.strptime(
        lowest["datetime"], strptime_format).replace(
        tzinfo=timezone)
    print(lowest_datetime)
    print(lowest_datetime.timestamp())
    lowest_in_last_days = (
        current_time - lowest_datetime).days
    median_datetime = datetime.datetime.strptime(
        median_time["datetime"], strptime_format).replace(
        tzinfo=timezone)
    print(median_datetime)
    median_in_last_days = (
        current_time - median_datetime).days
    message = "{0} received highest ping on {1} with value {2}ms in last {3} days".format(monitor.name,
                                                                                          highest["datetime"], highest["value"],
                                                                                          highest_in_last_days)
    print(message)
    message = "{0} received lowest ping on {1} with value {2}ms in last {3} days".format(monitor.name,
                                                                                         lowest["datetime"], lowest["value"],
                                                                                         lowest_in_last_days)
    print(message)
    message = "{0} received median ping on {1} with value {2}ms in last {3} days".format(monitor.name,
                                                                                         median_time["datetime"], median_time["value"],
                                                                                         median_in_last_days)
    print(message)
