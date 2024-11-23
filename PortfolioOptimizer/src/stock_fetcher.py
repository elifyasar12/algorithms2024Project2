import requests
import time


class StockFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"

    def fetch_stock_price(self, ticker):
        """Fetches the current price of a stock."""
        try:
            params = {
                "function": "GLOBAL_QUOTE",
                "symbol": ticker,
                "apikey": self.api_key
            }
            response = requests.get(self.base_url, params=params)
            data = response.json()
            if "Global Quote" in data and "05. price" in data["Global Quote"]:
                price = float(data["Global Quote"]["05. price"])
                print(f"Fetched price for {ticker}: {price}")
                return price
            else:
                print(f"Error: Unexpected response format for {ticker}")
                return None
        except Exception as e:
            print(f"Error fetching price for {ticker}: {e}")
            return None

    def fetch_portfolio_prices(self, tickers):
        """Fetches prices for a list of tickers, respecting API rate limits."""
        portfolio = {}
        for ticker in tickers:
            price = self.fetch_stock_price(ticker)
            if price:
                portfolio[ticker] = price
            time.sleep(2)  # Respect API rate limits (5 requests/minute)
        return portfolio
