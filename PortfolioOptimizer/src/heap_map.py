# import heapq
# import numpy as np


# class HeapMap:
#     def __init__(self, portfolio_values, asset_names):
#         """
#         Initializes the HeapMap with portfolio values and asset names.
#         :param portfolio_values: A 3D array (time steps × simulations × assets) of simulated portfolio values.
#         :param asset_names: A list of asset names corresponding to the dimensions in portfolio_values.
#         """
#         self.portfolio_values = portfolio_values
#         self.asset_names = asset_names

#     def calculate_asset_risks(self):
#         """
#         Calculates risk for each asset as the standard deviation of its daily returns.
#         Returns a list of tuples: [(risk, asset_name), ...].
#         """
#         # Transpose to extract asset values for each simulation
#         #asset_values = self.portfolio_values[:, :, :].transpose(2, 0, 1)  # Shape: (assets × time × simulations)
#         asset_values = self.portfolio_values.transpose(2, 0, 1)  # Shape: (assets × time × simulations)
#         risks = []

#         for i, asset in enumerate(self.asset_names):
#             # Calculate daily returns for this asset
#             daily_returns = np.diff(asset_values[i], axis=0) / asset_values[i][:-1]
#             # Calculate risk as the standard deviation of daily returns
#             risk = np.std(daily_returns)
#             risks.append((risk, asset))

#         return risks

#     def generate_heap(self):
#         """
#         Generates a max-heap of assets based on their calculated risks.
#         Returns a list sorted by descending risk values.
#         """
#         asset_risks = self.calculate_asset_risks()
#         max_heap = [(-risk, asset) for risk, asset in asset_risks]  # Negate risks for max-heap
#         heapq.heapify(max_heap)
#         return max_heap

#     def display_heap(self, heap):
#         """
#         Displays the heap in a readable format.
#         """
#         print("Heap Map: Areas of Higher Portfolio Risk")
#         print("-" * 50)
#         for neg_risk, asset in heap:
#             print(f"Asset: {asset}, Risk: {-neg_risk:.4f}")


# src/heap_map.py
# import heapq
# import numpy as np

# class HeapMap:
#     def __init__(self, portfolio_values, asset_names):
#         """
#         Initializes the HeapMap with portfolio values and asset names.

#         :param portfolio_values: A 3D array (time steps × simulations × assets) of
#                                  simulated portfolio values.
#         :param asset_names: A list of asset names corresponding to the dimensions in
#                             portfolio_values.
#         """
#         if portfolio_values.ndim != 3:
#             raise ValueError(
#                 f"Expected a 3D array for portfolio_values, got {portfolio_values.ndim}D"
#             )
#         if len(asset_names) != portfolio_values.shape[2]:
#             raise ValueError("Number of asset names must match the last dimension of portfolio_values.")
        
#         self.portfolio_values = portfolio_values
#         self.asset_names = asset_names

#     def calculate_asset_risks(self):
#         """
#         Calculates risk for each asset as the standard deviation of its daily returns.
#         Returns a list of tuples: [(risk, asset_name), ...].
#         """
#         # Extract asset values for each simulation
#         asset_values = self.portfolio_values.transpose(2, 0, 1)  # Shape: (assets × time × simulations)
#         risks = []

#         for i, asset in enumerate(self.asset_names):
#             # Calculate daily returns for this asset
#             daily_returns = np.diff(asset_values[i], axis=0) / asset_values[i][:-1]
#             # Calculate risk as the standard deviation of daily returns
#             risk = np.std(daily_returns)
#             risks.append((risk, asset))

#         return risks

#     def generate_heap(self):
#         """
#         Generates a max-heap of assets based on their calculated risks.
#         Returns a list sorted by descending risk values.
#         """
#         asset_risks = self.calculate_asset_risks()
#         max_heap = [(-risk, asset) for risk, asset in asset_risks]  # Negate risks for max-heap
#         heapq.heapify(max_heap)
#         return max_heap

#     def display_heap(self, heap):
#         """
#         Displays the heap in a readable format.
#         """
#         print("Heap Map: Areas of Higher Portfolio Risk")
#         print("-" * 50)
#         for neg_risk, asset in heap:
#             print(f"Asset: {asset}, Risk: {-neg_risk:.4f}")


# import heapq
# import numpy as np

# class HeapMap:
#     def __init__(self, portfolio_values, asset_names):
#         """
#         Initializes the HeapMap with portfolio values and asset names.
#         """
#         if portfolio_values.ndim != 3:
#             raise ValueError(f"Expected a 3D array for portfolio_values, got {portfolio_values.ndim}D")
#         if len(asset_names) != portfolio_values.shape[2]:
#             raise ValueError("Number of asset names must match the last dimension of portfolio_values.")

#         self.portfolio_values = portfolio_values
#         self.asset_names = asset_names

#     def calculate_asset_risks(self):
#         """
#         Calculates risk for each asset as the standard deviation of its daily returns.
#         Returns a list of tuples: [(risk, asset_name), ...].
#         """
#         asset_values = self.portfolio_values.transpose(2, 0, 1)  # Shape: (assets × time × simulations)
#         risks = []

#         for i, asset in enumerate(self.asset_names):
#             daily_returns = np.diff(asset_values[i], axis=0) / asset_values[i][:-1]
#             risk = np.std(daily_returns)
#             risks.append((risk, asset))

#         return risks

#     def generate_heap(self):
#         """
#         Generates a max-heap of assets based on their calculated risks.
#         Returns a list sorted by descending risk values.
#         """
#         asset_risks = self.calculate_asset_risks()
#         max_heap = [(-risk, asset) for risk, asset in asset_risks]
#         heapq.heapify(max_heap)
#         return max_heap

#     def display_heap(self, heap):
#         """
#         Displays the heap in a readable format.
#         """
#         print("Heap Map: Areas of Higher Portfolio Risk")
#         print("-" * 50)
#         for neg_risk, asset in heap:
#             print(f"Asset: {asset}, Risk: {-neg_risk:.4f}")

# import heapq
# import numpy as np

import numpy as np
import os
import matplotlib.pyplot as plt
import yfinance as yf
import heapq

class HeapMap:
    def __init__(self, portfolio_values, asset_names):
        if portfolio_values.ndim != 3:
            raise ValueError(f"Expected a 3D array for portfolio_values, got {portfolio_values.ndim}D")
        if len(asset_names) != portfolio_values.shape[2]:
            raise ValueError("Asset names must match the last dimension of portfolio_values.")
        self.portfolio_values = portfolio_values
        self.asset_names = asset_names

    def calculate_asset_risks(self):
        asset_values = self.portfolio_values.transpose(2, 0, 1)
        risks = []

        for i, asset in enumerate(self.asset_names):
            daily_returns = np.diff(asset_values[i], axis=0) / asset_values[i][:-1]
            risk = np.std(daily_returns)
            risks.append((risk, asset))

        return risks

    def generate_heap(self):
        asset_risks = self.calculate_asset_risks()
        max_heap = [(-risk, asset) for risk, asset in asset_risks]
        heapq.heapify(max_heap)
        return max_heap

    def display_heap(self, heap):
        print("Heap Map: Areas of Higher Portfolio Risk")
        print("-" * 50)
        for neg_risk, asset in heap:
            print(f"Asset: {asset}, Risk: {-neg_risk:.4f}")
