from pandas import DataFrame, Timestamp, to_datetime
from collections.abc import Sequence
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Union

DateLike = Union[str, datetime, Timestamp]

class Source(ABC):
    """Abstract base class for data sources."""

    def fetch(self, symbols: Sequence[str], start: DateLike, end: DateLike) -> DataFrame:
        """Fetch data for the given symbols between start and end dates."""

        start, end = self._normalise_dates(start, end)
        df = self.load(symbols, start, end)
        return df

    @staticmethod
    def _normalise_dates(start: DateLike, end: DateLike) -> tuple[Timestamp, Timestamp]:
        """Convert inputs to pandas Timestamps and ensure `start` < `end`."""

        pd_start, pd_end = to_datetime(start), to_datetime(end)

        if pd_start > pd_end:
            raise ValueError(f'Start date {pd_start} is after end date {pd_end}')

        return pd_start, pd_end
    
    @abstractmethod
    def load(self, symbols: Sequence[str], start: Timestamp, end: Timestamp) -> DataFrame:
        """Fetch raw data. Implementation required by subclass."""
        ...

    # Want to add a `meta` method later, not now though.