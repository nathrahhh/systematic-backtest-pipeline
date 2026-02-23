import yaml
import pandas as pd
import os
from src.data_loader import load_data
from src.signals import volatility_breakout_signal
from src.backtest import run_backtest
from src.performance import evaluate_strategy

with open("configs/base_config.yaml", "r") as f:
    config = yaml.safe_load(f)

df = load_data(config["data"]["path"])
signals = volatility_breakout_signal(df, config["strategy"])
results = run_backtest(df, signals, config["backtest"])
metrics = evaluate_strategy(results["NetStrategyReturn"])

print(metrics)  

results_row = {
    "k": config["strategy"]["k"],
    "atr_window": config["strategy"]["atr_window"],
    "holding_period": config["backtest"]["holding_period"],
    "cost": config["backtest"]["cost"],
    **metrics
}

log_file = "experiments_log.csv"

if os.path.exists(log_file):
    log_df = pd.read_csv(log_file)
    log_df = pd.concat([log_df, pd.DataFrame([results_row])], ignore_index=True)
else:
    log_df = pd.DataFrame([results_row])

log_df.to_csv(log_file, index=False)

