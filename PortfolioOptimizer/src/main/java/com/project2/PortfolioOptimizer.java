package com.project2;

import yahoofinance.Stock;
import yahoofinance.YahooFinance;
import org.apache.commons.math3.distribution.NormalDistribution;

import java.io.IOException;
import java.math.BigDecimal;
import java.util.*;

public class PortfolioOptimizer {

    private final List<String> tickers;
    private final Map<String, BigDecimal> stockPrices;

    public PortfolioOptimizer(List<String> tickers) {
        this.tickers = tickers;
        this.stockPrices = new HashMap<>();
    }

    // Fetch real-time stock prices
    public void fetchStockPrices() throws IOException {
        for (String ticker : tickers) {
            Stock stock = YahooFinance.get(ticker);
            if (stock != null && stock.getQuote().getPrice() != null) {
                stockPrices.put(ticker, stock.getQuote().getPrice());
                System.out.println("Fetched price for " + ticker + ": " + stock.getQuote().getPrice());
            } else {
                System.out.println("Could not fetch price for " + ticker);
            }
        }
    }

    // Monte Carlo Simulation
    public void runMonteCarloSimulation(int simulations, double initialInvestment) {
        Random random = new Random();
        NormalDistribution distribution = new NormalDistribution(0.001, 0.02); // Daily return (mean = 0.1%, SD = 2%)

        System.out.println("Running " + simulations + " Monte Carlo simulations...");
        double portfolioValue = initialInvestment;

        for (int i = 0; i < simulations; i++) {
            double simulatedReturn = 0.0;

            for (String ticker : tickers) {
                if (stockPrices.containsKey(ticker)) {
                    double randomReturn = distribution.sample();
                    simulatedReturn += stockPrices.get(ticker).doubleValue() * (1 + randomReturn);
                }
            }

            portfolioValue += simulatedReturn;
            System.out.printf("Simulation %d: Portfolio Value: %.2f%n", i + 1, portfolioValue);
        }
    }

    public static void main(String[] args) {
        List<String> tickers = Arrays.asList("AAPL", "GOOGL", "AMZN"); // Example tickers
        PortfolioOptimizer optimizer = new PortfolioOptimizer(tickers);

        try {
            optimizer.fetchStockPrices();
            optimizer.runMonteCarloSimulation(1000, 10000.0); // Simulate 1000 times with $10,000 initial investment
        } catch (IOException e) {
            System.err.println("Error fetching stock prices: " + e.getMessage());
        }
    }
}
