from src.stock_fetcher import StockFetcher
from src.monte_carlo import MonteCarloSimulator


if __name__ == "__main__":
    # Alpha Vantage API Key
    api_key = "QQ1BBACXBOTLITS9"

    # Initialize the StockFetcher
    fetcher = StockFetcher(api_key)

    # Define tickers and initial investment
    tickers = ["AAPL", "GOOGL", "AMZN"]
    initial_investment = 10000

    # Fetch stock prices
    portfolio_prices = fetcher.fetch_portfolio_prices(tickers)

    if not portfolio_prices:
        print("Error: Could not fetch any stock prices.")
    else:
        print(f"Portfolio prices: {portfolio_prices}")

        # Initialize MonteCarloSimulator
        simulator = MonteCarloSimulator(portfolio_prices, initial_investment)

        # Run simulation
        portfolio_values = simulator.simulate()

        if portfolio_values is not None:
            # Plot simulation results
            simulator.plot_simulation(portfolio_values)
