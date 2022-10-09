from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config, LetterCase
from diversio.model.monitor import Monitor
from diversio.model.response_times import ResponseTime
from diversio.utils import median


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class MonitorStats:
    """
    MonitorStats is the root model that is from api getMonitor of diversio.
    """
    monitor: Monitor
    timezone: str = "+00:00"

    def summary(self):
        highest, lowest, median_time, average_time = self.monitor.get_response_times_summary()
        message = "{0} received highest ping on {1} with value {2}ms in last {3} days" \
            .format(self.monitor.name,
                    highest.get_str_local_datetime(
                        self.timezone),
                    highest.value,
                    highest.get_last_days(self.timezone))
        print(message)
        message = "{0} received lowest ping on {1} with value {2}ms in last {3} days" \
            .format(self.monitor.name,
                    lowest.get_str_local_datetime(
                        self.timezone),
                    lowest.value,
                    lowest.get_last_days(self.timezone))
        print(message)
        message = "{0} received median ping on {1} with value {2}ms in last {3} days" \
            .format(self.monitor.name,
                    median_time.get_str_local_datetime(
                        self.timezone),
                    median_time.value,
                    median_time.get_last_days(self.timezone))
        print(message)

        message = "{0} average ping is {1}ms".format(
            self.monitor.name, average_time)
        print(message)
