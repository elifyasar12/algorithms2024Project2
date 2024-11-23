package com.project2;

import yahoofinance.Stock;
import yahoofinance.YahooFinance;
import org.apache.commons.math3.distribution.NormalDistribution;

import java.io.IOException;
import java.math.BigDecimal;
import java.util.*;

public class App {

    private static Map<String, BigDecimal> fetchStockPrices(List<String> tickers) throws IOException {
        Map<String, BigDecimal> stockPrices = new HashMap<>();
        for (String ticker : tickers) {
            Stock stock = YahooFinance.get(ticker);
            if (stock != null && stock.getQuote().getPrice() != null) {
                stockPrices.put(ticker, stock.getQuote().getPrice());
                System.out.println("Fetched price for " + ticker + ": " + stock.getQuote().getPrice());
            } else {
                System.out.println("Failed to fetch price for " + ticker);
            }
        }
        return stockPrices;
    }

    private static void runMonteCarloSimulation(Map<String, BigDecimal> stockPrices, int simulations, double initialInvestment) {
        Random random = new Random();
        NormalDistribution distribution = new NormalDistribution(0.001, 0.02); // Daily return with mean and SD

        System.out.println("Running Monte Carlo simulations...");
        for (int i = 0; i < simulations; i++) {
            double portfolioValue = initialInvestment;
            for (BigDecimal price : stockPrices.values()) {
                double simulatedReturn = distribution.sample();
                portfolioValue += price.doubleValue() * simulatedReturn;
            }
            System.out.printf("Simulation %d: Portfolio Value: %.2f%n", i + 1, portfolioValue);
        }
    }

    public static void main(String[] args) {
        List<String> tickers = Arrays.asList("AAPL", "GOOGL", "AMZN"); // Example tickers
        double initialInvestment = 10000.0;
        int simulations = 100;

        try {
            Map<String, BigDecimal> stockPrices = fetchStockPrices(tickers);
            runMonteCarloSimulation(stockPrices, simulations, initialInvestment);
        } catch (IOException e) {
            System.err.println("Error fetching stock data: " + e.getMessage());
        }
    }
}
