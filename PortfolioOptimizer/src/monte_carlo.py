# import numpy as np
# import matplotlib.pyplot as plt
# import os


# class MonteCarloSimulator:
#     def __init__(self, portfolio, initial_investment):
#         self.portfolio = portfolio
#         self.initial_investment = initial_investment

#     def simulate(self, num_simulations=500, time_horizon=250):
#         """Runs a Monte Carlo simulation for portfolio returns."""
#         if not self.portfolio:
#             print("Error: Portfolio is empty. Cannot run simulation.")
#             return None

#         # Initialize weights and daily returns
#         weights = np.array([1 / len(self.portfolio)] * len(self.portfolio))  # Equal weights
#         num_assets = len(self.portfolio)
#         daily_returns = np.random.normal(0.001, 0.02, (time_horizon, num_assets, num_simulations))

#         # Simulate portfolio values
#         # portfolio_values = np.zeros((time_horizon, num_simulations, num_assets))
#         # for i in range(num_simulations):
#         #     weighted_returns = daily_returns[:, j, i] @ weights  # Weighted sum of asset returns
#         #     cumulative_return = np.cumprod(1 + weighted_returns) - 1  # Cumulative portfolio return
#         #     portfolio_values[:, i] = self.initial_investment * (1 + cumulative_return)

#         portfolio_values = np.zeros((num_simulations, time_horizon, num_assets))
#         for i in range(1, time_horizon):
#             for j, (assest_name, assest_price) in enumerate(self.portfolio.items()):
#                 asset_daily_return = daily_returns[:, j, 1]
#                 cumulative_return = np.cumprod(1 + asset_daily_return) - 1
#                 #portfolio_values[:, i, j] = assest_price * (1 + cumulative_return)
#                 portfolio_values[j, i, :] = assest_price * (1 + cumulative_return)

#         return portfolio_values

#     def export_simulation_graph(self, portfolio_values, filename="monte_carlo_simulation.png"):
#         """Saves the Monte Carlo simulation results to a graph."""
#         output_dir = "graphs"
#         os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
#         filepath = os.path.join(output_dir, filename)

#         plt.figure(figsize=(10, 6))
#         plt.plot(portfolio_values, alpha=0.1, color='blue')
#         plt.title('Monte Carlo Simulation for Portfolio Returns')
#         plt.xlabel('Days')
#         plt.ylabel('Portfolio Value')
#         plt.grid()
#         plt.savefig(filepath)  # Save the plot as an image file
#         print(f"Simulation graph saved as {filepath}")
#         plt.show()


# import numpy as np

# class MonteCarloSimulator:
#     def __init__(self, portfolio, initial_investment):
#         self.portfolio = portfolio  # Dictionary: {'AssetName': Price}
#         self.initial_investment = initial_investment

#     def simulate(self, num_simulations=500, time_horizon=250):
#         """Runs a Monte Carlo simulation for portfolio returns."""
#         if not self.portfolio:
#             print("Error: Portfolio is empty. Cannot run simulation.")
#             return None

#         # Initialize weights and daily returns
#         weights = np.array([1 / len(self.portfolio)] * len(self.portfolio))  # Equal weights
#         num_assets = len(self.portfolio)
#         daily_returns = np.random.normal(0.001, 0.02, (time_horizon, num_assets, num_simulations))

#         # Simulate portfolio values for each asset
#         portfolio_values = np.zeros((time_horizon, num_simulations, num_assets))
#         asset_prices = np.array(list(self.portfolio.values()))

#         for i in range(num_assets):
#             # Simulate daily returns for each asset across simulations
#             cumulative_returns = np.cumprod(1 + daily_returns[:, i, :], axis=0) - 1
#             portfolio_values[:, :, i] = asset_prices[i] * (1 + cumulative_returns)

#         return portfolio_values

# src/monte_carlo.py
# import numpy as np
# import os
# import matplotlib.pyplot as plt

# class MonteCarloSimulator:
#     def __init__(self, portfolio, initial_investment):
#         self.portfolio = portfolio
#         self.initial_investment = initial_investment

#     def simulate(self, num_simulations=500, time_horizon=250):
#         """
#         Runs a Monte Carlo simulation for portfolio returns.
#         """
#         if not self.portfolio:
#             print("Error: Portfolio is empty. Cannot run simulation.")
#             return None

#         weights = np.array([1 / len(self.portfolio)] * len(self.portfolio))  # Equal weights
#         num_assets = len(self.portfolio)

#         # Simulate daily returns
#         daily_returns = np.random.normal(0.001, 0.02, (time_horizon, num_assets, num_simulations))
#         portfolio_values = np.zeros((time_horizon, num_simulations, num_assets))

#         asset_prices = np.array(list(self.portfolio.values()))
#         for i in range(num_assets):
#             cumulative_returns = np.cumprod(1 + daily_returns[:, i, :], axis=0) - 1
#             portfolio_values[:, :, i] = asset_prices[i] * (1 + cumulative_returns)

#         # Combine assets into total portfolio value per simulation
#         total_portfolio_values = portfolio_values.sum(axis=2)
#         return portfolio_values  # Preserve the 3D shape
    
    
# src/monte_carlo.py
# import numpy as np
# import os
# import matplotlib.pyplot as plt

# class MonteCarloSimulator:
#     def __init__(self, portfolio, initial_investment):
#         """
#         Initializes the Monte Carlo Simulator with portfolio and investment amount.
#         :param portfolio: Dictionary of asset prices.
#         :param initial_investment: Initial investment amount.
#         """
#         self.portfolio = portfolio
#         self.initial_investment = initial_investment

#     def simulate(self, num_simulations=500, time_horizon=250):
#         """
#         Runs a Monte Carlo simulation for portfolio returns.
#         :param num_simulations: Number of simulation runs.
#         :param time_horizon: Number of days to simulate.
#         :return: Simulated portfolio values (3D array).
#         """
#         if not self.portfolio:
#             print("Error: Portfolio is empty. Cannot run simulation.")
#             return None

#         weights = np.array([1 / len(self.portfolio)] * len(self.portfolio))  # Equal weights
#         num_assets = len(self.portfolio)

#         # Simulate daily returns
#         daily_returns = np.random.normal(0.001, 0.02, (time_horizon, num_assets, num_simulations))
#         portfolio_values = np.zeros((time_horizon, num_simulations, num_assets))

#         asset_prices = np.array(list(self.portfolio.values()))
#         for i in range(num_assets):
#             cumulative_returns = np.cumprod(1 + daily_returns[:, i, :], axis=0) - 1
#             portfolio_values[:, :, i] = asset_prices[i] * (1 + cumulative_returns)

#         # Combine assets into total portfolio value per simulation
#         return portfolio_values  # Preserve the 3D shape

#     def export_simulation_graph(self, portfolio_values, filename="monte_carlo_simulation.png"):
#         """
#         Saves the Monte Carlo simulation results to a graph.
#         :param portfolio_values: Simulated portfolio values (3D array).
#         :param filename: Filename to save the graph.
#         """
#         output_dir = "graphs"
#         os.makedirs(output_dir, exist_ok=True)
#         filepath = os.path.join(output_dir, filename)

#         # Plot the average portfolio value and value range
#         plt.figure(figsize=(10, 6))
#         plt.plot(portfolio_values.mean(axis=1), color='blue', label='Average Portfolio Value')
#         plt.fill_between(
#             range(portfolio_values.shape[0]),
#             portfolio_values.min(axis=1),
#             portfolio_values.max(axis=1),
#             color='blue',
#             alpha=0.1,
#             label='Range of Portfolio Values'
#         )
#         plt.title('Monte Carlo Simulation for Portfolio Returns')
#         plt.xlabel('Days')
#         plt.ylabel('Portfolio Value')
#         plt.legend()
#         plt.grid()
#         plt.savefig(filepath)
#         print(f"Simulation graph saved as {filepath}")
#         plt.show()

# import numpy as np
# import os
# import matplotlib.pyplot as plt
# import yfinance as yf
# import heapq
# class MonteCarloSimulator:
#     def __init__(self, portfolio, initial_investment):
#         if not portfolio or initial_investment <= 0:
#             raise ValueError("Invalid portfolio or initial investment.")
#         self.portfolio = portfolio
#         self.initial_investment = initial_investment

#     def simulate(self, num_simulations=500, time_horizon=250):
#         weights = np.array([1 / len(self.portfolio)] * len(self.portfolio))
#         asset_prices = np.array(list(self.portfolio.values()))
#         num_assets = len(self.portfolio)

#         daily_returns = np.random.normal(0.001, 0.02, (time_horizon, num_assets, num_simulations))
#         portfolio_values = np.zeros((time_horizon, num_simulations, num_assets))

#         for i in range(num_assets):
#             cumulative_returns = np.cumprod(1 + daily_returns[:, i, :], axis=0) - 1
#             portfolio_values[:, :, i] = asset_prices[i] * (1 + cumulative_returns)

#         return portfolio_values

#     # def export_simulation_graph(self, portfolio_values, filename="monte_carlo_simulation.png"):
#     #     os.makedirs("graphs", exist_ok=True)
#     #     filepath = os.path.join("graphs", filename)

#     #     plt.figure(figsize=(10, 6))
#     #     plt.plot(portfolio_values.mean(axis=1), color='blue', label='Average Portfolio Value')
#     #     plt.fill_between(
#     #         range(portfolio_values.shape[0]),
#     #         portfolio_values.min(axis=1),
#     #         portfolio_values.max(axis=1),
#     #         color='blue',
#     #         alpha=0.1,
#     #         label='Range of Portfolio Values'
#     #     )
#     #     plt.title('Monte Carlo Simulation for Portfolio Returns')
#     #     plt.xlabel('Days')
#     #     plt.ylabel('Portfolio Value')
#     #     plt.legend()
#     #     plt.grid()
#     #     plt.savefig(filepath)
#     #     print(f"Simulation graph saved as {filepath}")
#     #     plt.show()

# def export_simulation_graph(self, portfolio_values, filename="monte_carlo_simulation.png"):
#     os.makedirs("graphs", exist_ok=True)
#     filepath = os.path.join("graphs", filename)

#     # Aggregate portfolio values across simulations to get total portfolio value per time step
#     total_portfolio_values = portfolio_values.sum(axis=2)  # Sum across assets
#     avg_values = total_portfolio_values.mean(axis=1)  # Average across simulations
#     min_values = total_portfolio_values.min(axis=1)  # Minimum across simulations
#     max_values = total_portfolio_values.max(axis=1)  # Maximum across simulations

#     plt.figure(figsize=(10, 6))
#     plt.plot(avg_values, color='blue', label='Average Portfolio Value')
#     plt.fill_between(
#         range(len(avg_values)),
#         min_values,
#         max_values,
#         color='blue',
#         alpha=0.1,
#         label='Range of Portfolio Values'
#     )
#     plt.title('Monte Carlo Simulation for Portfolio Returns')
#     plt.xlabel('Days')
#     plt.ylabel('Portfolio Value')
#     plt.legend()
#     plt.grid()
#     plt.savefig(filepath)
#     print(f"Simulation graph saved as {filepath}")
#     plt.show()

# import numpy as np
# import os
# import matplotlib.pyplot as plt

# class MonteCarloSimulator:
#     def __init__(self, portfolio, initial_investment):
#         if not portfolio or initial_investment <= 0:
#             raise ValueError("Invalid portfolio or initial investment.")
#         self.portfolio = portfolio
#         self.initial_investment = initial_investment

#     def simulate(self, num_simulations=500, time_horizon=365):
#         weights = np.array([1 / len(self.portfolio)] * len(self.portfolio))
#         asset_prices = np.array(list(self.portfolio.values()))
#         num_assets = len(self.portfolio)

#         daily_returns = np.random.normal(0.001, 0.02, (time_horizon, num_assets, num_simulations))
#         portfolio_values = np.zeros((time_horizon, num_simulations, num_assets))

#         for i in range(num_assets):
#             cumulative_returns = np.cumprod(1 + daily_returns[:, i, :], axis=0) - 1
#             portfolio_values[:, :, i] = asset_prices[i] * (1 + cumulative_returns)

#         return portfolio_values

#     def export_simulation_graph(self, portfolio_values, filename="monte_carlo_simulation.png"):
#         os.makedirs("graphs", exist_ok=True)
#         filepath = os.path.join("graphs", filename)

#         # Aggregate portfolio values across simulations to get total portfolio value per time step
#         total_portfolio_values = portfolio_values.sum(axis=2)  # Sum across assets
#         avg_values = total_portfolio_values.mean(axis=1)  # Average across simulations
#         min_values = total_portfolio_values.min(axis=1)  # Minimum across simulations
#         max_values = total_portfolio_values.max(axis=1)  # Maximum across simulations

#         plt.figure(figsize=(10, 6))
#         plt.plot(avg_values, color='blue', label='Average Portfolio Value')
#         plt.fill_between(
#             range(len(avg_values)),
#             min_values,
#             max_values,
#             color='blue',
#             alpha=0.1,
#             label='Range of Portfolio Values'
#         )
#         plt.title('Monte Carlo Simulation for Portfolio Returns')
#         plt.xlabel('Days')
#         plt.ylabel('Portfolio Value')
#         plt.legend()
#         plt.grid()
#         plt.savefig(filepath)
#         print(f"Simulation graph saved as {filepath}")
#         plt.show()


# import numpy as np
# import os
# import matplotlib.pyplot as plt

# # Define S&P 500 data simulation (mocked for demonstration purposes)
# def sp500_simulation(time_horizon=365, initial_value=4000):
#     """
#     Simulates the S&P 500 performance for comparison.
#     """
#     daily_returns = np.random.normal(0.0005, 0.01, time_horizon)  # Approx historical daily mean and std deviation
#     sp500_values = initial_value * np.cumprod(1 + daily_returns)
#     return sp500_values

# # Define the Monte Carlo simulation
# class MonteCarloSimulator:
#     def __init__(self, portfolio, initial_investment):
#         if not portfolio or initial_investment <= 0:
#             raise ValueError("Invalid portfolio or initial investment.")
#         self.portfolio = portfolio
#         self.initial_investment = initial_investment

#     def simulate(self, num_simulations=500, time_horizon=365):
#         weights = np.array([1 / len(self.portfolio)] * len(self.portfolio))
#         asset_prices = np.array(list(self.portfolio.values()))
#         num_assets = len(self.portfolio)

#         daily_returns = np.random.normal(0.001, 0.02, (time_horizon, num_assets, num_simulations))
#         portfolio_values = np.zeros((time_horizon, num_simulations, num_assets))

#         for i in range(num_assets):
#             cumulative_returns = np.cumprod(1 + daily_returns[:, i, :], axis=0) - 1
#             portfolio_values[:, :, i] = asset_prices[i] * (1 + cumulative_returns)

#         return portfolio_values

#     def export_simulation_with_sp500_graph(self, portfolio_values, sp500_values, filename="monte_carlo_vs_sp500.png"):
#         os.makedirs("graphs", exist_ok=True)
#         filepath = os.path.join("graphs", filename)

#         # Aggregate portfolio values across simulations to get total portfolio value per time step
#         total_portfolio_values = portfolio_values.sum(axis=2)  # Sum across assets
#         avg_values = total_portfolio_values.mean(axis=1)  # Average across simulations
#         min_values = total_portfolio_values.min(axis=1)  # Minimum across simulations
#         max_values = total_portfolio_values.max(axis=1)  # Maximum across simulations

#         plt.figure(figsize=(12, 8))
#         # Plot portfolio simulation results
#         plt.plot(avg_values, color='blue', label='Portfolio Avg. Value')
#         plt.fill_between(
#             range(len(avg_values)),
#             min_values,
#             max_values,
#             color='blue',
#             alpha=0.1,
#             label='Portfolio Value Range'
#         )

#         # Plot S&P 500 results
#         plt.plot(sp500_values, color='green', label='S&P 500 Performance', linestyle='--')

#         plt.title('Monte Carlo Simulation vs S&P 500 Performance')
#         plt.xlabel('Days')
#         plt.ylabel('Portfolio Value')
#         plt.legend()
#         plt.grid()
#         plt.savefig(filepath)
#         print(f"Simulation graph with S&P 500 saved as {filepath}")
#         plt.show()

# # Mock portfolio and initial investment for testing
# portfolio = {"Asset 1": 100, "Asset 2": 200, "Asset 3": 300}
# initial_investment = 1000

# # Create an instance of the Monte Carlo Simulator
# simulator = MonteCarloSimulator(portfolio, initial_investment)
# portfolio_values = simulator.simulate()

# # Generate simulated S&P 500 data
# sp500_values = sp500_simulation()

# # Export the graph
# simulator.export_simulation_with_sp500_graph(portfolio_values, sp500_values)


import numpy as np
import os
import matplotlib.pyplot as plt


class MonteCarloSimulator:
    def __init__(self, portfolio, initial_investment):
        if not portfolio or initial_investment <= 0:
            raise ValueError("Invalid portfolio or initial investment.")
        self.portfolio = portfolio
        self.initial_investment = initial_investment

    # def simulate(self, num_simulations=500, time_horizon=365):
    #     weights = np.array([1 / len(self.portfolio)] * len(self.portfolio))
    #     asset_prices = np.array(list(self.portfolio.values()))
    #     num_assets = len(self.portfolio)

    #     #daily_returns = np.random.normal(0.001, 0.02, (time_horizon, num_assets, num_simulations))
    #     daily_returns = np.random.normal(0.001, np.random.uniform(0.01, 0.05, num_assets).reshape(-1, 1, 1), (time_horizon, num_assets, num_simulations))

    #     portfolio_values = np.zeros((time_horizon, num_simulations, num_assets))

    #     for i in range(num_assets):
    #         cumulative_returns = np.cumprod(1 + daily_returns[:, i, :], axis=0) - 1
    #         portfolio_values[:, :, i] = asset_prices[i] * (1 + cumulative_returns)

    #     return portfolio_values

    def simulate(self, num_simulations=500, time_horizon=365):
        weights = np.array([1 / len(self.portfolio)] * len(self.portfolio))
        asset_prices = np.array(list(self.portfolio.values()))
        num_assets = len(self.portfolio)

        # Generate daily returns with per-asset variability
        asset_volatility = np.random.uniform(0.01, 0.05, num_assets)  # Volatility per asset
        daily_returns = np.random.normal(
            loc=0.001,  # Mean return
            scale=asset_volatility[:, np.newaxis],  # np.newaxis# Broadcast volatility for time and simulations
            size=(time_horizon, num_assets, num_simulations)
    )

        portfolio_values = np.zeros((time_horizon, num_simulations, num_assets))

        for i in range(num_assets):
            cumulative_returns = np.cumprod(1 + daily_returns[:, i, :], axis=0) - 1
            portfolio_values[:, :, i] = asset_prices[i] * (1 + cumulative_returns)

        return portfolio_values


    def export_simulation_graph(self, portfolio_values, filename="monte_carlo_simulation.png"):
        os.makedirs("graphs", exist_ok=True)
        filepath = os.path.join("graphs", filename)

        total_portfolio_values = portfolio_values.sum(axis=2)  # Sum across assets
        avg_values = total_portfolio_values.mean(axis=1)  # Average across simulations
        min_values = total_portfolio_values.min(axis=1)  # Minimum across simulations
        max_values = total_portfolio_values.max(axis=1)  # Maximum across simulations

        plt.figure(figsize=(10, 6))
        plt.plot(avg_values, color='blue', label='Average Portfolio Value')
        plt.fill_between(
            range(len(avg_values)),
            min_values,
            max_values,
            color='blue',
            alpha=0.1,
            label='Range of Portfolio Values'
        )
        plt.title('Monte Carlo Simulation for Portfolio Returns')
        plt.xlabel('Days')
        plt.ylabel('Portfolio Value')
        plt.legend()
        plt.grid()
        plt.savefig(filepath)
        print(f"Simulation graph saved as {filepath}")
        plt.show()

    def export_snp_comparison_graph(self, portfolio_values, snp_returns, filename="monte_carlo_vs_snp.png"):
        os.makedirs("graphs", exist_ok=True)
        filepath = os.path.join("graphs", filename)

        total_portfolio_values = portfolio_values.sum(axis=2)  # Sum across assets
        avg_values = total_portfolio_values.mean(axis=1)  # Average across simulations

        # Simulate S&P 500 cumulative returns
        snp_cumulative = np.cumprod(1 + snp_returns) * self.initial_investment

        plt.figure(figsize=(10, 6))
        plt.plot(avg_values, color='blue', label='Simulated Portfolio (Average)')
        plt.plot(snp_cumulative, color='green', linestyle='--', label='S&P 500 Benchmark')
        plt.title('Monte Carlo Simulation vs S&P 500')
        plt.xlabel('Days')
        plt.ylabel('Portfolio Value')
        plt.legend()
        plt.grid()
        plt.savefig(filepath)
        print(f"S&P 500 comparison graph saved as {filepath}")
        plt.show()


