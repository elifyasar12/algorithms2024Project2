import numpy as np
import matplotlib.pyplot as plt


class MonteCarloSimulator:
    def __init__(self, portfolio, initial_investment):
        self.portfolio = portfolio
        self.initial_investment = initial_investment

    def simulate(self, num_simulations=1000, time_horizon=252):
        """Runs a Monte Carlo simulation for portfolio returns."""
        if not self.portfolio:
            print("Error: Portfolio is empty. Cannot run simulation.")
            return None

        # Initialize weights and daily returns
        weights = np.array([1 / len(self.portfolio)] * len(self.portfolio))  # Equal weights
        num_assets = len(self.portfolio)
        daily_returns = np.random.normal(0.001, 0.02, (time_horizon, num_assets, num_simulations))

        # Simulate portfolio values
        portfolio_values = np.zeros((time_horizon, num_simulations))
        for i in range(num_simulations):
            weighted_returns = daily_returns[:, :, i] @ weights  # Weighted sum of asset returns
            cumulative_return = np.cumprod(1 + weighted_returns) - 1  # Cumulative portfolio return
            portfolio_values[:, i] = self.initial_investment * (1 + cumulative_return)

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
