import json
import fake_data
import diversio_stats
import datetime
import locale
from utils import _dict, median
from unittest import TestCase, main
from unittest.mock import Mock, patch
from functools import reduce

class TestDiversioStatus(TestCase):
    def _mock_response(self, status=200, json_data=None, raise_for_status = None):
        mock_resp = Mock()

        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        
        mock_resp.status_code = status

        if json_data:
            mock_resp.json = Mock(return_value = _dict(json_data))
        
        return mock_resp

    @patch("requests.get")
    def test_uptime_robot_dashboard(self, mock_get):
        psp_api_path="https://stats.uptimerobot.com/api/getMonitor/Q5ogPt6JAQ?m=785837216"
        json_data = fake_data.fake_data_json()
        mock_resp = self._mock_response(json_data = json_data)

        mock_get.side_effect = [mock_resp]
        response, value = diversio_stats.get(psp_api_path)

        self.assertEqual(value.title, "Diversio Status")

        monitor = _dict(value.monitor)

        self.assertIsNotNone(monitor.responseTimes)

        sorted_response_times = sorted(monitor.responseTimes, key = lambda x: x["value"],reverse=True)
        highest = sorted_response_times[0]
        lowest = sorted_response_times[-1]
        median_time = median(sorted_response_times)

        strptime_format = "%B %d, %Y, %H:%M"

        highest_datetime = datetime.datetime.strptime(highest["datetime"], strptime_format )
        a = (datetime.datetime.now() - datetime.datetime.strptime(highest["datetime"], strptime_format)) 
        highest_in_last_days = (datetime.datetime.now() - datetime.datetime.strptime(highest["datetime"], strptime_format)).days 
        lowest_datetime =  datetime.datetime.strptime(lowest["datetime"], strptime_format)
        lowest_in_last_days = (datetime.datetime.now() - datetime.datetime.strptime(lowest["datetime"], strptime_format)).days 
        median_datetime =  datetime.datetime.strptime(median_time["datetime"], strptime_format)
        median_in_last_days = (datetime.datetime.now() - datetime.datetime.strptime(median_time["datetime"],strptime_format)).days 
        # highest
        self.assertEqual(highest["value"], 296)
        message = "{0} received highest ping on {1} with value {2}ms in last {3} days".format(monitor.name, \
            highest["datetime"], highest["value"], \
            highest_in_last_days )
        print(message)
        # min
        self.assertEqual(lowest["value"], 213)
        message = "{0} received lowest ping on {1} with value {2}ms in last {3} days".format(monitor.name, \
            lowest["datetime"], lowest["value"], \
            lowest_in_last_days)
        print(message)
        # # median
        self.assertEqual(median_time["value"], 226)
        message = "{0} received median ping on {1} with value {2}ms in last {3} days".format(monitor.name, \
            median_time["datetime"], median_time["value"], \
            median_in_last_days)
        print(message)

if __name__=="__main__":
    main()