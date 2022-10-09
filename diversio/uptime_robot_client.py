import requests
from diversio.model.monitor_stats import MonitorStats


class UptimeRobotClient():
    def get(self, url):
        try:
            response = requests.get(url=url)
            if response.status_code != 200:
                raise
        except requests.exceptions.RequestException as e:
            print(str(e))

        response.raise_for_status()
        return response.json()

    def run(self, url):
        response = self.get(url)
        monitor_stats = MonitorStats(response)

        monitor_stats.summary()
