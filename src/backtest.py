import numpy as np

def build_positions(df, holding_period=5):
    df = df.copy()
    df["Position"] = 0

    positions = df["Position"].values
    signals = df["Signal"].values

    for t in range(len(df)):
        if signals[t] != 0:
            start = t + 1
            end = min(t + 1 + holding_period, len(df))
            positions[start:end] += signals[t]

    df["Position"] = positions
    return df


def compute_strategy_returns(df, cost_per_trade=0.001):
    df = df.copy()

    df["Return"] = df["Close"].pct_change()
    df["StrategyReturn"] = df["Position"].shift(1) * df["Return"]
    df["Turnover"] = df["Position"].diff().abs()
    df["Cost"] = df["Turnover"] * cost_per_trade
    df["NetStrategyReturn"] = df["StrategyReturn"] - df["Cost"]

    return df


def run_backtest(df, signals, backtest_config):
    df = df.copy()
    df["Signal"] = signals

    df = build_positions(
        df,
        holding_period=backtest_config["holding_period"]
    )

    df = compute_strategy_returns(
        df,
        cost_per_trade=backtest_config["cost"]
    )

    return df
