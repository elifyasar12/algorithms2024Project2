# from src.stock_fetcher import StockFetcher
# from src.monte_carlo import MonteCarloSimulator
# from src.risk_metrics import RiskMetrics

# if __name__ == "__main__":
#     # Alpha Vantage API Key 1
#     #api_key = "QQ1BBACXBOTLITS9"
#     # Alpha Vantage API Key 2
#     api_key = "CVZD7QN0CGBL9161"

#     # Initialize the StockFetcher
#     fetcher = StockFetcher(api_key)

#     # Define tickers and initial investment
#     tickers = ["AAPL", "GOOGL", "AMZN", "FDX"]
#     initial_investment = 10000

#     # Fetch stock prices
#     portfolio_prices = fetcher.fetch_portfolio_prices(tickers)

#     if not portfolio_prices:
#         print("Error: Could not fetch any stock prices.")
#     else:
#         print(f"Portfolio prices: {portfolio_prices}")

#         # Initialize MonteCarloSimulator
#         simulator = MonteCarloSimulator(portfolio_prices, initial_investment)

#         # Run simulation
#         portfolio_values = simulator.simulate(num_simulations=100, time_horizon=50)

#         if portfolio_values is not None:
#             # Export simulation graph
#             simulator.export_simulation_graph(portfolio_values)

#             # Analyze Risk
#             risk_metrics = RiskMetrics(portfolio_values)

#             # Calculate and display Value at Risk (VaR)
#             risk_metrics.calculate_var(confidence_level=0.95)

#             # Plot and save portfolio value distribution
#             risk_metrics.plot_distribution()


# from src.stock_fetcher import StockFetcher
# from src.monte_carlo import MonteCarloSimulator
# from src.risk_metrics import RiskMetrics

# if __name__ == "__main__":
#     # Initialize the StockFetcher
#     fetcher = StockFetcher()

#     # Define tickers and initial investment
#     tickers = ["AAPL", "GOOGL", "AMZN", "FDX"]
#     initial_investment = 10000

#     # Fetch stock prices
#     portfolio_prices = fetcher.fetch_portfolio_prices(tickers)

#     if not portfolio_prices:
#         print("Error: Could not fetch any stock prices.")
#     else:
#         print(f"Portfolio prices: {portfolio_prices}")

#         # Initialize MonteCarloSimulator
#         simulator = MonteCarloSimulator(portfolio_prices, initial_investment)

#         # Run simulation
#         portfolio_values = simulator.simulate(num_simulations=500, time_horizon=250)

#         if portfolio_values is not None:
#             # Export simulation graph
#             simulator.export_simulation_graph(portfolio_values)

#             # Analyze Risk
#             risk_metrics = RiskMetrics(portfolio_values)

#             # Calculate and display Value at Risk (VaR)
#             risk_metrics.calculate_var(confidence_level=0.95)

#             # Plot and save portfolio value distribution
#             risk_metrics.plot_distribution()


# from src.stock_fetcher import StockFetcher
# from src.monte_carlo import MonteCarloSimulator
# from src.risk_metrics import RiskMetrics
# from src.heap_map import HeapMap

# if __name__ == "__main__":
#     # Initialize the StockFetcher
#     fetcher = StockFetcher()

#     # Define tickers and initial investment
#     tickers = ["AAPL", "GOOGL", "AMZN", "FDX"]
#     initial_investment = 10000

#     # Fetch stock prices
#     portfolio_prices = fetcher.fetch_portfolio_prices(tickers)

#     if not portfolio_prices:
#         print("Error: Could not fetch any stock prices.")
#     else:
#         print(f"Portfolio prices: {portfolio_prices}")

#         # Initialize MonteCarloSimulator
#         simulator = MonteCarloSimulator(portfolio_prices, initial_investment)

#         # Run simulation
#         portfolio_values = simulator.simulate(num_simulations=100, time_horizon=50)

#         if portfolio_values is not None:
#             # Export simulation graph
#             simulator.export_simulation_graph(portfolio_values)

#             # Analyze Risk
#             risk_metrics = RiskMetrics(portfolio_values)
#             risk_metrics.calculate_var(confidence_level=0.95)
#             risk_metrics.plot_distribution()

#             # Visualize Risk via Heat Map
#             # heatmap = RiskHeatMap(portfolio_values, len(portfolio_prices))
#             # daily_risk = heatmap.calculate_daily_risk()
#             # heatmap.plot_heatmap(daily_risk)

#             # Visualize Risk via Heap Map
#             heap_map = HeapMap(portfolio_values, len(portfolio_prices))
#             heap = heap_map.generate_heap()
#             heap_map.display_heap(heap)

# from src.stock_fetcher import StockFetcher
# from src.monte_carlo import MonteCarloSimulator
# from src.risk_metrics import RiskMetrics
# from src.heap_map import HeapMap

# if __name__ == "__main__":
#     # Initialize the StockFetcher
#     fetcher = StockFetcher()

#     # Define tickers and initial investment
#     tickers = ["AAPL", "GOOGL", "AMZN", "FDX"]
#     initial_investment = 10000

#     # Fetch stock prices
#     portfolio_prices = fetcher.fetch_portfolio_prices(tickers)

#     if not portfolio_prices:
#         print("Error: Could not fetch any stock prices.")
#     else:
#         print(f"Portfolio prices: {portfolio_prices}")

#         # Initialize MonteCarloSimulator
#         simulator = MonteCarloSimulator(portfolio_prices, initial_investment)

#         # Run simulation
#         portfolio_values = simulator.simulate(num_simulations=500, time_horizon=250)

#         if portfolio_values is not None:
#             # Export simulation graph
#             simulator.export_simulation_graph(portfolio_values)

#             # Analyze Risk
#             risk_metrics = RiskMetrics(portfolio_values)
#             risk_metrics.calculate_var(confidence_level=0.95)
#             risk_metrics.plot_distribution()

#             # Visualize Risk via Heap Map
#             heap_map = HeapMap(portfolio_values, tickers)
#             heap = heap_map.generate_heap()
#             heap_map.display_heap(heap)


# from src.stock_fetcher import StockFetcher
# from src.monte_carlo import MonteCarloSimulator
# from src.risk_metrics import RiskMetrics
# from src.heap_map import HeapMap

# if __name__ == "__main__":
#     # Initialize the StockFetcher
#     fetcher = StockFetcher()

#     # Define tickers and initial investment
#     tickers = ["AAPL", "GOOGL", "AMZN", "FDX"]
#     initial_investment = 10000

#     # Fetch stock prices
#     portfolio_prices = fetcher.fetch_portfolio_prices(tickers)

#     if not portfolio_prices:
#         print("Error: Could not fetch any stock prices.")
#     else:
#         print(f"Portfolio prices: {portfolio_prices}")

#         # Initialize MonteCarloSimulator
#         simulator = MonteCarloSimulator(portfolio_prices, initial_investment)

#         # Run simulation
#         portfolio_values = simulator.simulate(num_simulations=500, time_horizon=250)

#         if portfolio_values is not None:
#             # Export simulation graph
#             simulator.export_simulation_graph(portfolio_values)

#             # Analyze Risk
#             risk_metrics = RiskMetrics(portfolio_values)
#             risk_metrics.calculate_var(confidence_level=0.95)
#             risk_metrics.plot_distribution()

#             # Visualize Risk via Heap Map
#             heap_map = HeapMap(portfolio_values, tickers)
#             heap = heap_map.generate_heap()
#             heap_map.display_heap(heap)


# from src.stock_fetcher import StockFetcher
# from src.monte_carlo import MonteCarloSimulator
# from src.risk_metrics import RiskMetrics
# from src.heap_map import HeapMap

# if __name__ == "__main__":
#     # Initialize the StockFetcher
#     fetcher = StockFetcher()

#     # Define tickers and initial investment
#     tickers = ["AAPL", "GOOGL", "AMZN", "FDX"]
#     initial_investment = 10000

#     # Fetch stock prices
#     portfolio_prices = fetcher.fetch_portfolio_prices(tickers)

#     if not portfolio_prices:
#         print("Error: Could not fetch any stock prices.")
#     else:
#         print(f"Portfolio prices: {portfolio_prices}")

#         # Initialize MonteCarloSimulator
#         simulator = MonteCarloSimulator(portfolio_prices, initial_investment)

#         # Run simulation
#         portfolio_values = simulator.simulate(num_simulations=500, time_horizon=250)

#         if portfolio_values is not None:
#             # Export simulation graph
#             simulator.export_simulation_graph(portfolio_values)

#             # Analyze Risk
#             risk_metrics = RiskMetrics(portfolio_values)
#             risk_metrics.calculate_var(confidence_level=0.95)
#             risk_metrics.plot_distribution()

#             # Visualize Risk via Heap Map
#             heap_map = HeapMap(portfolio_values, tickers)
#             heap = heap_map.generate_heap()
#             heap_map.display_heap(heap)

# from src.stock_fetcher import StockFetcher
# from src.monte_carlo import MonteCarloSimulator
# from src.risk_metrics import RiskMetrics
# from src.heap_map import HeapMap


# if __name__ == "__main__":
#     fetcher = StockFetcher()
#     tickers = ["AAPL", "GOOGL", "AMZN", "FDX"]
#     initial_investment = 10000

#     portfolio_prices = fetcher.fetch_portfolio_prices(tickers)
#     if portfolio_prices:
#         simulator = MonteCarloSimulator(portfolio_prices, initial_investment)
#         portfolio_values = simulator.simulate()

#         if portfolio_values is not None:
#             simulator.export_simulation_graph(portfolio_values)

#             risk_metrics = RiskMetrics(portfolio_values)
#             risk_metrics.calculate_var()
#             risk_metrics.plot_distribution()

#             heap_map = HeapMap(portfolio_values, tickers)
#             heap = heap_map.generate_heap()
#             heap_map.display_heap(heap)


from src.stock_fetcher import StockFetcher
from src.monte_carlo import MonteCarloSimulator
from src.risk_metrics import RiskMetrics
from src.heap_map import HeapMap


if __name__ == "__main__":
    fetcher = StockFetcher()
    tickers = ["AAPL", "GOOGL", "AMZN", "FDX"]
    initial_investment = 10000

    portfolio_prices = fetcher.fetch_portfolio_prices(tickers)
    if portfolio_prices:
        simulator = MonteCarloSimulator(portfolio_prices, initial_investment)
        portfolio_values = simulator.simulate()

        if portfolio_values is not None:
            simulator.export_simulation_graph(portfolio_values)

            risk_metrics = RiskMetrics(portfolio_values)
            risk_metrics.calculate_var()
            risk_metrics.plot_distribution()

            heap_map = HeapMap(portfolio_values, tickers)
            heap = heap_map.generate_heap()
            heap_map.display_heap(heap)
            #heap_map.display_heap(heap)
            heap_map.export_treemap(heap)
            heap_map.export_heap_tree(heap)
