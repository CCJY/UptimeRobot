import datetime
from diversio.model.base import Base
from diversio.model.monitor import Monitor
from diversio.model.response_times import ResponseTime
from diversio.utils import median


class MonitorStats(Base):
    def validate(self):
        pass

    def get_timezone(self):
        if self.timezone:
            return self.timezone

        return "+00:00"

    def get_monitor(self) -> Monitor:
        if not self.monitor:
            raise ValueError("The monitor field is none")
        if isinstance(self.monitor, Monitor):
            return self.monitor
        else:
            raise ValueError("The monitor field is not instance of monitor")

    def summary(self):
        highest, lowest, median_time = self.get_monitor().get_response_times_summary()
        message = "{0} received highest ping on {1} with value {2}ms in last {3} days" \
            .format(self.monitor.name,
                    highest.get_str_local_datetime(
                        self.get_timezone()),
                    highest.value,
                    highest.get_last_days(self.get_timezone()))
        print(message)
        message = "{0} received lowest ping on {1} with value {2}ms in last {3} days" \
            .format(self.monitor.name,
                    lowest.get_str_local_datetime(
                        self.get_timezone()),
                    lowest.value,
                    lowest.get_last_days(self.get_timezone()))
        print(message)
        message = "{0} received median ping on {1} with value {2}ms in last {3} days" \
            .format(self.monitor.name,
                    median_time.get_str_local_datetime(
                        self.get_timezone()),
                    median_time.value,
                    median_time.get_last_days(self.get_timezone()))
        print(message)
