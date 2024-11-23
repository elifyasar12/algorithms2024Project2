from src.portfolio_optimizer import PortfolioOptimizer

if __name__ == "__main__":
    # Alpha Vantage API Key
    api_key = "QQ1BBACXBOTLITS9"
    optimizer = PortfolioOptimizer(api_key)

    # Tickers and initial investment
    tickers = ["AAPL", "GOOGL", "AMZN"]
    initial_investment = 10000

    # Run Monte Carlo Simulation
    portfolio_values = optimizer.monte_carlo_simulation(tickers, initial_investment)

    # Check if simulation data exists before proceeding
    if portfolio_values is not None:
        # Calculate VaR
        optimizer.calculate_var(portfolio_values, confidence_level=0.95)
    else:
        print("Portfolio simulation could not be completed due to missing data.")
