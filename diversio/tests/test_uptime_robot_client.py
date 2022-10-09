from unittest import TestCase
from unittest.mock import Mock, patch
from diversio.tests.fake_data import fake_data_json
from diversio.uptime_robot_client import UptimeRobotClient
from diversio.utils import _dict
from diversio.model.monitor_stats import MonitorStats


class TestUptimeRobotClient(TestCase):
    def _mock_response(self, status=200, json_data=None, raise_for_status=None):
        mock_resp = Mock()

        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status

        mock_resp.status_code = status

        if json_data:
            mock_resp.json = Mock(return_value=_dict(json_data))

        return mock_resp

    @patch("requests.get")
    def test_uptime_robot_client_monitor(self, mock_get):
        psp_api_path = "https://stats.uptimerobot.com/api/getMonitor/Q5ogPt6JAQ?m=785837216"
        json_data = fake_data_json()
        mock_resp = self._mock_response(json_data=json_data)

        mock_get.side_effect = [mock_resp]
        response = UptimeRobotClient().get(psp_api_path)

        monitor_stats = MonitorStats(response)

        highest, lowest, median_time = monitor_stats.monitor.get_response_times_summary()

        self.assertEqual(highest.value, 296)
        self.assertEqual(lowest.value, 211)
        self.assertEqual(median_time.value, 223)

        monitor_stats.summary()
