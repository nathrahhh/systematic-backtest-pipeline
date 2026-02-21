import yaml
from src.data_loader import load_data
from src.signals import generate_signal
from src.backtest import run_backtest
from src.performance import compute_metrics

with open("configs/base_config.yaml", "r") as f:
    config = yaml.safe_load(f)

df = load_data(config["data"]["path"])
signals = generate_signal(df, config["strategy"])
results = run_backtest(df, signals, config["backtest"])
metrics = compute_metrics(results)

print(metrics)
