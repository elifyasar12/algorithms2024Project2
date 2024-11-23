from src.portfolio_optimizer import PortfolioOptimizer

if __name__ == "__main__":
    api_key = "QQ1BBACXBOTLITS9"
    optimizer = PortfolioOptimizer(api_key)

    tickers = ["AAPL", "GOOGL", "AMZN"]
    initial_investment = 10000

    optimizer.monte_carlo_simulation(tickers, initial_investment)
