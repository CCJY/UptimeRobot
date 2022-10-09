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

    def get_local_datetime(self, timezone: str = None) -> datetime.datetime:
        dt = self._get_datetime(timezone=timezone)

        return dt.astimezone()

    def get_str_local_datetime(self, timezone: str = None) -> datetime.datetime:
        dt = self.get_local_datetime(timezone=timezone)

        return datetime.datetime.strftime(dt, self.strftime_format)

