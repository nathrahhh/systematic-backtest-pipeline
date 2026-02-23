import numpy as np
import pandas as pd
from src.features import compute_atr

def volatility_breakout_signal(df, strategy_config):

    df = compute_atr(df, window=strategy_config["atr_window"])

    k = strategy_config["k"]
    strategy_type = strategy_config["type"]

    breakout_mask = df["Range"] > k * df["ATR"]

    signal = pd.Series(0, index=df.index)

    if strategy_type == "trend":
        # Follow the move
        direction = np.sign(df["Close"] - df["Open"])
        signal[breakout_mask] = direction[breakout_mask]

    elif strategy_type == "mean_reversion":
        # Fade the move
        direction = -np.sign(df["Close"] - df["Open"])
        signal[breakout_mask] = direction[breakout_mask]

    return signal
