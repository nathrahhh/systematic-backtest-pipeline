import yaml
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
