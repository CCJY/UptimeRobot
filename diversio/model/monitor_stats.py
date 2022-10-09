import datetime
from diversio.model.base import Base
from diversio.model.response_times import ResponseTime
from diversio.utils import median


class MonitorStats(Base):
    def validate(self):
        pass

    def get_timezone(self):
        if self.timezone:
            return self.timezone

        return "+00:00"

    strptime_format = "%B %d, %Y, %H:%M%z"
    strftime_format = "%B %d, %Y, %H:%M"

    def str_response_time_detail(self, response_time: ResponseTime):
        if response_time.datetime:
            current_time = datetime.datetime.now(datetime.timezone.utc)
            dt = datetime.datetime.strptime(
                response_time.datetime + self.get_timezone(), self.strptime_format)
            last_days = (current_time - dt).days

            message = "{0} received highest ping on {1} with value {2}ms in last {3} days" \
                .format(self.monitor.name,
                        datetime.datetime.strftime(
                            dt.astimezone(), self.strftime_format),
                        # response_time.datetime,
                        response_time.value,
                        last_days)
            return message

        return ""

    def summary(self):
        highest, lowest, median_time = self.monitor.get_response_times_summary()

        print(self.str_response_time_detail(highest))
        print(self.str_response_time_detail(lowest))
        print(self.str_response_time_detail(median_time))
