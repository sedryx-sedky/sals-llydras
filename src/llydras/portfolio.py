from collections.abc import Sequence
from typing import Union
from sources import Source, yFinanceSource
from pandas import DataFrame, Timestamp

class Portfolio:
    def __init__(self, symbols: Sequence[str], source: Union[Source, None] = None):
        self.symbols = tuple(tickers)
        self.source = source or yFinanceSource()

        self.shares: Union[DataFrame, None] = None
        self.prices: Union[DataFrame, None] = None

        self._cash: float = 0

        self.date: Union[Timestamp, None] = None

    @property
    def cash(self):
        return self._cash

    def __update_cash(self, delta: float):
        if delta < 0 and self._cash + delta < 0:
            raise Exception

        self._cash += delta

    def deposit(self, cash: float):
        self._update_cash(amount)

    def withdraw(self, weight: float = None, cash: float = None):
        if weight is None and cash is None:
            raise Exception
        elif weight is not None and cash is not None:
            raise Exception

        if weight is not None:
            if not (0 < weight <= 1):
                raise Exception

            self.__update_cash(-self._cash * weight)
        else:
            self.__update_cash(-cash)

    def buy(self, fraction, cash, shares):
        ...

    def sell(self, fraction, cash, shares):
        ...

    def trade(self, start: DateLike, end: DateLike):
        self.source.fetch(start, end)
        