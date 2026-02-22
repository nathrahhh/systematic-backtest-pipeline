import numpy as np
import pandas as pd
from src.features import compute_atr

def volatility_breakout_signal(df, strategy_config):
    df = compute_atr(df, window=strategy_config["atr_window"])

    k = strategy_config["k"]

    breakout_mask = df["Range"] > k * df["ATR"]

    signal = pd.Series(0, index=df.index)

    directional_move = np.sign(df["Close"] - df["Open"])

    signal[breakout_mask] = directional_move[breakout_mask]

    return signal

