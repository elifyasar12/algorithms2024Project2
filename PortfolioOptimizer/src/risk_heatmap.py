# # import numpy as np
# # import matplotlib.pyplot as plt
# # import os


# # class RiskHeatMap:
# #     def __init__(self, portfolio_values, num_assets):
# #         self.portfolio_values = portfolio_values
# #         self.num_assets = num_assets

# #     def calculate_daily_risk(self):
# #         """
# #         Calculates the standard deviation of daily returns across simulations.
# #         Returns a matrix of daily risk values (time x assets).
# #         """
# #         if self.portfolio_values is None:
# #             print("Error: No portfolio values provided.")
# #             return None

# #         # Calculate daily returns from portfolio values
# #         daily_returns = np.diff(self.portfolio_values, axis=0) / self.portfolio_values[:-1]

# #         # Compute standard deviation of returns across simulations for each asset
# #         daily_risk = np.std(daily_returns, axis=1)  # Shape: (time_horizon-1, num_assets)
# #         return daily_risk

# #     def plot_heatmap(self, daily_risk, filename="risk_heatmap.png"):
# #         """
# #         Generates and saves a heat map of portfolio risk.
# #         """
# #         if daily_risk is None:
# #             print("Error: No risk data to plot.")
# #             return

# #         output_dir = "graphs"
# #         os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
# #         filepath = os.path.join(output_dir, filename)

# #         reshaped_risk = np.expand_dims(daily_risk, axis=0)

# #         # Generate the heat map
# #         plt.figure(figsize=(12, 8))
# #         plt.imshow(daily_risk.T, aspect='auto', cmap='coolwarm', origin='lower')
# #         plt.colorbar(label='Risk (Standard Deviation)')
# #         plt.title('Portfolio Risk Heat Map')
# #         plt.xlabel('Time (Days)')
# #         plt.ylabel('Assets')
# #         plt.xticks(ticks=np.arange(0, daily_risk.shape[0], step=10), labels=np.arange(0, daily_risk.shape[0], step=10))
# #         plt.yticks(ticks=np.arange(self.num_assets), labels=[f"Asset {i+1}" for i in range(self.num_assets)])
# #         plt.grid(False)
# #         plt.savefig(filepath)
# #         print(f"Risk heat map saved to: {filepath}")
# #         plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import os


# class RiskHeatMap:
#     def __init__(self, portfolio_values, num_assets):
#         self.portfolio_values = portfolio_values
#         self.num_assets = num_assets

#     def calculate_daily_risk(self):
#         """
#         Calculates the standard deviation of daily returns across simulations.
#         Returns a vector of daily risk values (time_horizon-1).
#         """
#         if self.portfolio_values is None:
#             print("Error: No portfolio values provided.")
#             return None

#         # Calculate daily returns from portfolio values
#         daily_returns = np.diff(self.portfolio_values, axis=0) / self.portfolio_values[:-1]

#         # Compute standard deviation of daily returns across simulations
#         daily_risk = np.std(daily_returns, axis=1)  # Shape: (time_horizon-1,)
#         return daily_risk

#     def plot_heatmap(self, daily_risk, filename="risk_heatmap.png"):
#         """
#         Generates and saves a heat map of portfolio risk.
#         """
#         if daily_risk is None:
#             print("Error: No risk data to plot.")
#             return

#         output_dir = "graphs"
#         os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
#         filepath = os.path.join(output_dir, filename)

#         # Reshape daily_risk for heat map (if necessary, e.g., 2D representation)
#         reshaped_risk = np.expand_dims(daily_risk, axis=0)  # Convert to 2D for heat map

#         # Generate the heat map
#         plt.figure(figsize=(12, 2))  # Adjust dimensions for horizontal visualization
#         plt.imshow(reshaped_risk, aspect='auto', cmap='coolwarm', origin='lower')
#         plt.colorbar(label='Risk (Standard Deviation)')
#         plt.title('Portfolio Risk Over Time')
#         plt.xlabel('Time (Days)')
#         plt.yticks([])  # No asset-specific rows in this representation
#         plt.savefig(filepath)
#         print(f"Risk heat map saved to: {filepath}")
#         plt.show()

