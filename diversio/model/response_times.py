from dataclasses import dataclass
import datetime
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ResponseTime:
    """
    ResponseTime class is the data model

    Attributes:
        datetime: str
            The datetime's format is "%B %d, %Y, %H:%M%z" (like October 08, 2022, 04:00)
        value: int
            The value is about latency
    """
    datetime: str
    value: int

    strptime_with_tz_format = "%B %d, %Y, %H:%M%z"
    strptime_format = "%B %d, %Y, %H:%M"
    strftime_format = "%B %d, %Y, %H:%M"

    def _get_datetime(self, timezone: str = None) -> datetime.datetime:
        if not self.datetime:
            raise ValueError("The datetime field is none")
        if timezone:
            return datetime.datetime.strptime(
                self.datetime + timezone, self.strptime_with_tz_format
            )
        return datetime.datetime.strptime(
            self.datetime, self.strptime_format
        )

    def get_local_datetime(self, timezone: str = None) -> datetime.datetime:
        dt = self._get_datetime(timezone=timezone)

        return dt.astimezone()

    def get_str_local_datetime(self, timezone: str = None) -> datetime.datetime:
        dt = self.get_local_datetime(timezone=timezone)

        return datetime.datetime.strftime(dt, self.strftime_format)

    def get_last_days(self, timezone: str = None) -> int:
        """Get last days.

        The function calculates between current datetime and class member's datetime

        Args:
            timezone (str, optional): timezone like "+05:00". Defaults to None.

        Returns:
            int: days
        """
        if timezone:
            current_time = datetime.datetime.now().astimezone()
        else:
            current_time = datetime.datetime.now()

        dt = self.get_local_datetime(timezone=timezone)
        return (current_time - dt).days
