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

# import numpy as np
# import os
# import matplotlib.pyplot as plt
# import yfinance as yf
# import heapq

# class HeapMap:
#     def __init__(self, portfolio_values, asset_names):
#         if portfolio_values.ndim != 3:
#             raise ValueError(f"Expected a 3D array for portfolio_values, got {portfolio_values.ndim}D")
#         if len(asset_names) != portfolio_values.shape[2]:
#             raise ValueError("Asset names must match the last dimension of portfolio_values.")
#         self.portfolio_values = portfolio_values
#         self.asset_names = asset_names

#     def calculate_asset_risks(self):
#         asset_values = self.portfolio_values.transpose(2, 0, 1)
#         risks = []

#         for i, asset in enumerate(self.asset_names):
#             daily_returns = np.diff(asset_values[i], axis=0) / asset_values[i][:-1]
#             risk = np.std(daily_returns)
#             risks.append((risk, asset))

#         return risks

#     def generate_heap(self):
#         asset_risks = self.calculate_asset_risks()
#         max_heap = [(-risk, asset) for risk, asset in asset_risks]
#         heapq.heapify(max_heap)
#         return max_heap

#     def display_heap(self, heap):
#         print("Heap Map: Areas of Higher Portfolio Risk")
#         print("-" * 50)
#         for neg_risk, asset in heap:
#             print(f"Asset: {asset}, Risk: {-neg_risk:.4f}")


# import heapq
# import numpy as np

# import numpy as np
# import os
# import matplotlib.pyplot as plt
# import yfinance as yf
# import heapq
# class HeapMap:
#     def __init__(self, portfolio_values, asset_names):
#         if portfolio_values.ndim != 3:
#             raise ValueError(f"Expected a 3D array for portfolio_values, got {portfolio_values.ndim}D")
#         if len(asset_names) != portfolio_values.shape[2]:
#             raise ValueError("Asset names must match the last dimension of portfolio_values.")
#         self.portfolio_values = portfolio_values
#         self.asset_names = asset_names

#     def calculate_asset_risks(self):
#         asset_values = self.portfolio_values.transpose(2, 0, 1)
#         risks = []

#         for i, asset in enumerate(self.asset_names):
#             daily_returns = np.diff(asset_values[i], axis=0) / asset_values[i][:-1]
#             risk = np.std(daily_returns)
#             risks.append((risk, asset))

#         return risks

#     def generate_heap(self):
#         asset_risks = self.calculate_asset_risks()
#         max_heap = [(-risk, asset) for risk, asset in asset_risks]
#         heapq.heapify(max_heap)
#         return max_heap

#     def display_heap(self, heap):
#         print("Heap Map: Areas of Higher Portfolio Risk")
#         print("-" * 50)
#         for neg_risk, asset in heap:
#             print(f"Asset: {asset}, Risk: {-neg_risk:.4f}")

#     def export_heap_map_graph(self, heap, filename="heap_map_graph.png"):
#         """
#         Generates and saves a bar graph to visualize risks from the heap.
#         """
#         os.makedirs("graphs", exist_ok=True)
#         filepath = os.path.join("graphs", filename)

#         # Extract data from the heap
#         risks = [-risk for risk, asset in heap]
#         assets = [asset for risk, asset in heap]

#         # Plotting the bar chart
#         plt.figure(figsize=(10, 6))
#         plt.bar(assets, risks, color='orange', alpha=0.7)
#         plt.title('Heap Map: Asset Risks')
#         plt.xlabel('Assets')
#         plt.ylabel('Risk (Standard Deviation)')
#         plt.xticks(rotation=45)
#         plt.grid(axis='y', linestyle='--', alpha=0.7)
#         plt.tight_layout()
#         plt.savefig(filepath)
#         print(f"Heap map graph saved as {filepath}")
#         plt.show()

import numpy as np
import os
import matplotlib.pyplot as plt
import yfinance as yf
import heapq
import squarify  # Install this with `pip install squarify`
import networkx as nx


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
            #daily_returns = np.diff(asset_values[i], axis=0) / asset_values[i][:-1]
            daily_returns = np.diff(asset_values[i], axis=0) / asset_values[i][:-1]
            #print(f"Asset: {asset}, Daily Returns Sample: {daily_returns[:5]}")

            #risk = np.std(daily_returns)
            risk = np.std(daily_returns) + np.abs(np.mean(daily_returns))  # Combines volatility and average return
            print(f"Asset: {asset}, Daily Returns Sample: {daily_returns[:5]}")
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

    def export_treemap(self, heap, filename="heap_treemap.png"):
        """
        Exports a treemap visualization of the heap.
        """
        os.makedirs("graphs", exist_ok=True)
        filepath = os.path.join("graphs", filename)

        # Extract data from the heap
        risks = [-risk for risk, asset in heap]
        assets = [asset for risk, asset in heap]

        # Normalize risks for treemap sizing
        total_risk = sum(risks)
        sizes = [risk / total_risk for risk in risks]

        # Plot treemap
        plt.figure(figsize=(10, 6))
        squarify.plot(
            sizes=sizes,
            label=[f"{asset}\nRisk: {risk:.4f}" for asset, risk in zip(assets, risks)],
            color=plt.cm.viridis(sizes),  # Color based on size
            alpha=0.7
        )
        plt.axis("off")
        plt.title("Asset Risks Treemap", fontsize=18)
        plt.savefig(filepath)
        print(f"Treemap graph saved as {filepath}")
        plt.show()

    # def export_heap_tree(self, heap, filename="heap_tree.png"):
    #     """
    #     Exports a tree visualization of the heap.
    #     """
    #     os.makedirs("graphs", exist_ok=True)
    #     filepath = os.path.join("graphs", filename)

    #     G = nx.DiGraph()  # Directed graph for heap

    #     # Create a binary tree from the heap
    #     for i, (neg_risk, asset) in enumerate(heap):
    #         G.add_node(i, label=f"{asset}\nRisk: {-neg_risk:.4f}")
    #         left = 2 * i + 1
    #         right = 2 * i + 2
    #         if left < len(heap):
    #             G.add_edge(i, left)
    #         if right < len(heap):
    #             G.add_edge(i, right)

    #     # Draw the graph
    #     pos = nx.nx_agraph.graphviz_layout(G, prog="dot")  # Use Graphviz for tree layout
    #     labels = nx.get_node_attributes(G, "label")

    #     plt.figure(figsize=(12, 8))
    #     nx.draw(
    #         G,
    #         pos,
    #         labels=labels,
    #         with_labels=True,
    #         node_size=2000,
    #         node_color="lightblue",
    #         font_size=8,
    #         font_weight="bold",
    #         arrows=False,
    #     )
    #     plt.title("Heap Tree Visualization", fontsize=18)
    #     plt.savefig(filepath)
    #     print(f"Heap tree graph saved as {filepath}")
    #     plt.show()

    def export_heap_tree(self, heap, filename="heap_tree.png"):
        """
        Exports a tree visualization of the heap using spring layout.
        """
        os.makedirs("graphs", exist_ok=True)
        filepath = os.path.join("graphs", filename)

        G = nx.DiGraph()  # Directed graph for heap

        # Create a binary tree from the heap
        for i, (neg_risk, asset) in enumerate(heap):
            G.add_node(i, label=f"{asset}\nRisk: {-neg_risk:.4f}")
            left = 2 * i + 1
            right = 2 * i + 2
        if left < len(heap):
            G.add_edge(i, left)
        if right < len(heap):
            G.add_edge(i, right)

        # Use spring layout (no external dependencies required)
        pos = nx.spring_layout(G, seed=42)
        labels = nx.get_node_attributes(G, "label")

        plt.figure(figsize=(12, 8))
        nx.draw(
            G,
            pos,
            labels=labels,
            with_labels=True,
            node_size=2000,
            node_color="lightblue",
            font_size=8,
            font_weight="bold",
            arrows=False,
        )
        plt.title("Heap Tree Visualization", fontsize=18)
        plt.savefig(filepath)
        print(f"Heap tree graph saved as {filepath}")
        plt.show()
