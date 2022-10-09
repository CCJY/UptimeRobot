import requests
from diversio.utils.extracts_from_html import get_extract_from_html
from diversio.model.monitor_stats import MonitorStats


class UptimeRobotClient:
    """UptimeRobotClient class for diversio monitor status
    """
    extract_var = "pspApiPath"

    def _get_api_from_html(self, url):
        return get_extract_from_html(url, self.extract_var)

    def get(self, url):
        """Sends a Get request to api getMonitor of diversio.

        Args:
            url (_type_): str

        Returns:
            _type_: json of response
        """
        try:
            response = requests.get(url=url)
            if response.status_code != 200:
                raise
        except requests.exceptions.RequestException as e:
            print(str(e))

        response.raise_for_status()
        return response.json()

    def run(self, url):
        """Run uptime robot client

        it extracts the input value API endpoint from url related to HTML and then 
        calculates the result values after importing the data through the API endpoint.

        Lastly, it display monitor status summary.

        Args:
            url (_type_): str
        """
        api_url = self._get_api_from_html(url)
        response = self.get(api_url)
        monitor_stats = MonitorStats.from_dict(response)

        monitor_stats.summary()
