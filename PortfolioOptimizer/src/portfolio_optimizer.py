import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


class PortfolioOptimizer:
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
            price = float(data["Global Quote"]["05. price"])
            print(f"Fetched price for {ticker}: {price}")
            
            # Add delay to respect API limits
            time.sleep(12)  # 5 requests per minute
            return price
        except KeyError:
            print(f"Error: Could not fetch price for {ticker}")
            return None

    def monte_carlo_simulation(self, tickers, initial_investment, num_simulations=1000, time_horizon=252):
        """Runs a Monte Carlo simulation for portfolio returns."""
        # Fetch stock prices
        portfolio = {}
        for ticker in tickers:
            price = self.fetch_stock_price(ticker)
            if price:
                portfolio[ticker] = price

        if not portfolio:
            print("Error: No valid stock data fetched.")
            return None  # Return None if no stock data is fetched

        # Initialize weights and daily returns
        weights = np.array([1 / len(portfolio)] * len(portfolio))  # Equal weights
        num_assets = len(portfolio)
        daily_returns = np.random.normal(0.001, 0.02, (time_horizon, num_assets, num_simulations))

        # Simulate portfolio values
        portfolio_values = np.zeros((time_horizon, num_simulations))
        for i in range(num_simulations):
            weighted_returns = daily_returns[:, :, i] @ weights  # Weighted sum of asset returns
            cumulative_return = np.cumprod(1 + weighted_returns) - 1  # Cumulative portfolio return
            portfolio_values[:, i] = initial_investment * (1 + cumulative_return)

        # Plot results
        self.plot_simulation(portfolio_values)
        return portfolio_values

    def plot_simulation(self, portfolio_values):
        """Plots the Monte Carlo simulation results."""
        plt.figure(figsize=(10, 6))
        plt.plot(portfolio_values, alpha=0.1, color='blue')
        plt.title('Monte Carlo Simulation for Portfolio Returns')
        plt.xlabel('Days')
        plt.ylabel('Portfolio Value')
        plt.grid()
        plt.show()

    def calculate_var(self, portfolio_values, confidence_level=0.95):
        """Calculates the Value at Risk (VaR) at a given confidence level."""
        # Get the final portfolio values from all simulations
        final_values = portfolio_values[-1, :]
        
        # Calculate the percentiles for the given confidence level
        var = np.percentile(final_values, (1 - confidence_level) * 100)
        print(f"Value at Risk (VaR) at {confidence_level * 100}% confidence: {var:.2f}")
        return var
