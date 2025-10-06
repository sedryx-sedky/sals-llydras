from pandas import Timestamp, DataFrame
from collections.abc import Sequence
from .base import Source

from yfinance import download

class yFinanceSource(Source):
	def load(self, symbols: Sequence[str], start: Timestamp, end: Timestamp) -> DataFrame:
		tickers = ' '.join(symbols)
		prices = yf.download(tickers, start = start, end = end, interval = '1d')
		return prices['Close']