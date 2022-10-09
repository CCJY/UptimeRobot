import requests
from diversio.utils.extracts_from_html import get_extract_from_html
from diversio.model.monitor_stats import MonitorStats


class UptimeRobotClient:
    extract_var = "pspApiPath"

    def _get_api_from_html(self, url):
        return get_extract_from_html(url, self.extract_var)

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
        api_url = self._get_api_from_html(url)
        response = self.get(api_url)
        monitor_stats = MonitorStats(response)

        monitor_stats.summary()
