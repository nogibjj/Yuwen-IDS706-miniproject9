"""Script to run descriptive statistics on the iris dataset,
using common fucntions from lib.py"""
import pandas as pd
import lib


def run_descriptive_stats(data_: pd.DataFrame, target_column: str) -> dict:
    "Runs descriptive statistics on the passed dataset"
    return lib.get_data_descriptive_stats(data_,target_column)

def run_visualizations(data_: pd.DataFrame, target_var: str) -> None:
    "Runs visualizations on the passed dataset"
    lib.plot_hist(data_, target_var, jupyter=False)


if __name__ == '__main__':
    data = lib.load_data("src/iris_data.csv")
    TARGET_COLUMN = "SepalLengthCm"
    results = run_descriptive_stats(data, TARGET_COLUMN)
    print(results)
    run_visualizations(data, TARGET_COLUMN)