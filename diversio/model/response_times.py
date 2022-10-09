from diversio.model.base import Base


class ResponseTime(Base):
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
