# import numpy as np
# import matplotlib.pyplot as plt
# import os


# class RiskMetrics:
#     def __init__(self, portfolio_values):
#         self.portfolio_values = portfolio_values

#     def calculate_var(self, confidence_level=0.95):
#         """Calculates the Value at Risk (VaR) at a given confidence level."""
#         if self.portfolio_values is None:
#             print("Error: No portfolio values provided.")
#             return None

#         # Get the final portfolio values from all simulations
#         final_values = self.portfolio_values[-1, :]

#         # Calculate the percentile for the given confidence level
#         var = np.percentile(final_values, (1 - confidence_level) * 100)
#         print(f"Value at Risk (VaR) at {confidence_level * 100}% confidence: {var:.3f}")
#         return var

#     def plot_distribution(self, filename="final_portfolio_distribution.png"):
#         """Plots a histogram of the final portfolio values."""
#         if self.portfolio_values is None:
#             print("Error: No portfolio values provided.")
#             return

#         # Get the final portfolio values from all simulations
#         final_values = self.portfolio_values[-1, :]

#         # Create output directory
#         output_dir = "graphs"
#         os.makedirs(output_dir, exist_ok=True)

#         # Plot the histogram
#         plt.figure(figsize=(10, 6))
#         plt.hist(final_values, bins=50, color='blue', edgecolor='black', alpha=0.7)
#         plt.title('Distribution of Final Portfolio Values')
#         plt.xlabel('Portfolio Value')
#         plt.ylabel('Frequency')
#         plt.grid()
#         output_path = os.path.join(output_dir, filename)
#         plt.savefig(output_path)
#         print(f"Portfolio distribution graph saved to: {output_path}")
#         plt.show()

# import numpy as np
# import os
# import matplotlib.pyplot as plt

# class RiskMetrics:
#     def __init__(self, portfolio_values):
#         self.portfolio_values = portfolio_values

#     def calculate_var(self, confidence_level=0.95):
#         """
#         Calculates the Value at Risk (VaR) at a given confidence level.
#         """
#         if self.portfolio_values is None:
#             print("Error: No portfolio values provided.")
#             return None

#         # Get the final portfolio values from all simulations
#         final_values = self.portfolio_values[-1, :].sum(axis=1)
#         var = np.percentile(final_values, (1 - confidence_level) * 100)
#         print(f"Value at Risk (VaR) at {confidence_level * 100}% confidence: {var:.3f}")
#         return var

#     def plot_distribution(self, filename="final_portfolio_distribution.png"):
#         """
#         Plots a histogram of the final portfolio values.
#         """
#         if self.portfolio_values is None:
#             print("Error: No portfolio values provided.")
#             return

#         # Get the final portfolio values from all simulations
#         final_values = self.portfolio_values[-1, :].sum(axis=1)

#         # Create output directory
#         output_dir = "graphs"
#         os.makedirs(output_dir, exist_ok=True)

#         # Plot the histogram
#         plt.figure(figsize=(10, 6))
#         plt.hist(final_values, bins=50, color='blue', edgecolor='black', alpha=0.7)
#         plt.title('Distribution of Final Portfolio Values')
#         plt.xlabel('Portfolio Value')
#         plt.ylabel('Frequency')
#         plt.grid()
#         output_path = os.path.join(output_dir, filename)
#         plt.savefig(output_path)
#         print(f"Portfolio distribution graph saved to: {output_path}")
#         plt.show()

import numpy as np
import os
import matplotlib.pyplot as plt
import yfinance as yf
import heapq

class RiskMetrics:
    def __init__(self, portfolio_values):
        if portfolio_values is None or not portfolio_values.size:
            raise ValueError("Invalid portfolio values.")
        self.portfolio_values = portfolio_values

    def calculate_var(self, confidence_level=0.95):
        final_values = self.portfolio_values[-1, :].sum(axis=1)
        var = np.percentile(final_values, (1 - confidence_level) * 100)
        print(f"Value at Risk (VaR) at {confidence_level * 100}% confidence: {var:.3f}")
        return var

    def plot_distribution(self, filename="final_portfolio_distribution.png"):
        final_values = self.portfolio_values[-1, :].sum(axis=1)
        os.makedirs("graphs", exist_ok=True)

        plt.figure(figsize=(10, 6))
        plt.hist(final_values, bins=50, color='blue', edgecolor='black', alpha=0.7)
        plt.title('Distribution of Final Portfolio Values')
        plt.xlabel('Portfolio Value')
        plt.ylabel('Frequency')
        plt.grid()
        filepath = os.path.join("graphs", filename)
        plt.savefig(filepath)
        print(f"Portfolio distribution graph saved to: {filepath}")
        plt.show()

