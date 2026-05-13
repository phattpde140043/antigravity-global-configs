---
name: backtesting-frameworks
description: "Expert in building robust backtesting systems for trading strategies. Focuses on bias prevention and reliable performance estimation."
---

# Backtesting Frameworks

Build production-grade systems to validate trading strategies using historical data.

## Core Philosophy
A backtest is an experiment, not a promise. Treat historical data with extreme caution.

## Bias Prevention (The Killers of Strategies)
- **Look-ahead Bias**: DO NOT use information from the future to make decisions in the past (e.g., using "close" price to trade at "open").
- **Survivorship Bias**: Ensure the dataset includes delisted or bankrupt companies, not just current survivors.
- **Overfitting**: Limit the number of strategy parameters; use out-of-sample testing effectively.
- **Transaction Costs**: Always include realistic slippage, commission, and latency models.

## Backtest Architecture
- **Event-Driven vs Vectorized**:
    - Use **Event-Driven** for complex strategies, limit orders, and realistic latency simulation.
    - Use **Vectorized** (e.g., NumPy/Pandas) for fast research on simple signals.
- **Point-in-Time Data**: Maintain a data pipeline that reflects exactly what was known at each historical timestamp.

## Validation & Robustness
- **Walk-Forward Analysis**: Use a rolling window of training and testing data to simulate real-world usage.
- **Monte Carlo Simulation**: Resample returns to understand the range of possible outcomes and drawdown risks.
- **Metrics**: focus on **Sharpe/Sortino Ratio**, **Max Drawdown**, **Calmar Ratio**, and **Profit Factor**.

## Verification Checklist
- [ ] Is look-ahead bias completely eliminated via proper data indexing?
- [ ] Are slippage and commissions modeled realistically?
- [ ] Has the strategy been tested on out-of-sample data?
- [ ] Are delisted assets included in the universe?
