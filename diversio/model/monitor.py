from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config, LetterCase
from typing import List, Tuple
from diversio.utils import median
from diversio.model.log import Log
from diversio.model.response_times import ResponseTime


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Monitor:
    """
    Monitor class is the model that is from api getMonitor of diversio.
    """

    name: str
    logs: List[Log] = field(default_factory=list)
    response_times: List[ResponseTime] = field(default_factory=list)

    def get_response_times_summary(self) -> Tuple[ResponseTime, ResponseTime, ResponseTime, int]:
        """Get highest, lowest, and median of objects and average time

        Returns:
            Tuple[ResponseTime, ResponseTime, ResponseTime, int]: highest, lowest, median, average
        """
        sorted_response_times = sorted(
            self.response_times, key=lambda x: x.value, reverse=True)
        highest = sorted_response_times[0]
        lowest = sorted_response_times[-1]
        median_time = median(sorted_response_times)

        average_time = round(sum(
            [x.value for x in sorted_response_times]) / len(sorted_response_times), 2)

        return highest, lowest, median_time, average_time
