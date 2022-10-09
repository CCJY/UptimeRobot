from typing import Tuple
from diversio.utils import median
from diversio.model.base import Base
from diversio.model.log import Log
from diversio.model.response_times import ResponseTime


class Monitor(Base):
    def __init__(self, d):
        if d:
            if d.get("logs"):
                self.logs = []
                for log in d.get("logs"):
                    self.logs.append(Log(log))
            if d.get("responseTimes"):
                self.response_times = []
                for response_time in d.get("responseTimes"):
                    self.response_times.append(ResponseTime(response_time))
            if d.get("name"):
                self.name = d.get("name")

    def validate(self):
        pass

    def get_name(self):
        return self.name

    def get_response_times_summary(self) -> Tuple[ResponseTime, ResponseTime, ResponseTime, int]:
        sorted_response_times = sorted(
            self.response_times, key=lambda x: x.value, reverse=True)
        highest = sorted_response_times[0]
        lowest = sorted_response_times[-1]
        median_time = median(sorted_response_times)

        average_time = round(sum(
            [x.value for x in sorted_response_times]) / len(sorted_response_times), 2)

        return highest, lowest, median_time, average_time
