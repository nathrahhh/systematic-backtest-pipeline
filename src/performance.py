import numpy as np
import pandas as pd


TRADING_DAYS = 252


def compute_cagr(returns: pd.Series) -> float:
    """
    Compute Compound Annual Growth Rate (CAGR)
    Assumes returns are daily simple returns.
    """
    cumulative_return = (1 + returns).prod()
    n_years = len(returns) / TRADING_DAYS
    return cumulative_return ** (1 / n_years) - 1


def compute_annualized_volatility(returns: pd.Series) -> float:
    """
    Annualized volatility of daily returns.
    """
    return returns.std() * np.sqrt(TRADING_DAYS)


def compute_sharpe(returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    """
    Annualized Sharpe ratio.
    """
    excess_returns = returns - (risk_free_rate / TRADING_DAYS)
    ann_return = excess_returns.mean() * TRADING_DAYS
    ann_vol = excess_returns.std() * np.sqrt(TRADING_DAYS)

    if ann_vol == 0:
        return np.nan

    return ann_return / ann_vol


def compute_max_drawdown(returns: pd.Series) -> float:
    """
    Maximum drawdown from cumulative equity curve.
    """
    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()


def compute_worst_5pct_average(returns: pd.Series) -> float:
    """
    Average of worst 5% daily returns.
    """
    threshold = returns.quantile(0.05)
    worst_returns = returns[returns <= threshold]
    return worst_returns.mean()


def evaluate_strategy(returns: pd.Series) -> dict:
    """
    Master evaluation function.
    """
    return {
        "CAGR": compute_cagr(returns),
        "Annualized Volatility": compute_annualized_volatility(returns),
        "Sharpe Ratio": compute_sharpe(returns),
        "Max Drawdown": compute_max_drawdown(returns),
        "Worst 5% Avg Return": compute_worst_5pct_average(returns),
    }

