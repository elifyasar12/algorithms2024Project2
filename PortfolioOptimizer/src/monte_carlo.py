import numpy as np
import matplotlib.pyplot as plt
import os


class MonteCarloSimulator:
    def __init__(self, portfolio, initial_investment):
        self.portfolio = portfolio
        self.initial_investment = initial_investment

    def simulate(self, num_simulations=100, time_horizon=50):
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

    def export_simulation_graph(self, portfolio_values, filename="monte_carlo_simulation.png"):
        """Saves the Monte Carlo simulation results to a graph."""
        output_dir = "graphs"
        os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
        filepath = os.path.join(output_dir, filename)

        plt.figure(figsize=(10, 6))
        plt.plot(portfolio_values, alpha=0.1, color='blue')
        plt.title('Monte Carlo Simulation for Portfolio Returns')
        plt.xlabel('Days')
        plt.ylabel('Portfolio Value')
        plt.grid()
        plt.savefig(filepath)  # Save the plot as an image file
        print(f"Simulation graph saved as {filepath}")
        plt.show()
