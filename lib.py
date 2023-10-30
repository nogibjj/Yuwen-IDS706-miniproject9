import pandas as pd
import matplotlib.pyplot as plt


def load_data(datapath):
    return pd.read_csv(datapath)

def get_data_descriptive_stats(dataframe, col):
    """print column statistics"""
    data = dataframe[col]
    statistics = {
        'Mean': data.mean(numeric_only=True),
        'Median': data.median(numeric_only=True),
        'StdDev': data.std(numeric_only=True),
        'Min': data.min(numeric_only=True),
        'Max': data.max(numeric_only=True)
    }
    return pd.Series(statistics)

def plot_hist(dataframe, col,jupyter:bool=False):
    """Plot histogram of the given column"""
    plt.figure(figsize=(3.1104,2.0736))
    plt.hist(dataframe[col], bins=10, color='green', edgecolor='black', linewidth=1.2)
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    if not jupyter:
        visualization_path = 'output/visualization_hist.png'
        plt.savefig(visualization_path)  # save png
    else:
        plt.show()
    

if __name__ == "__main__":
    data = load_data("src/Iris.csv")
    TARGET_COLUMN = "SepalLengthCm"

    print('Target Column: ', TARGET_COLUMN)
    print('Statistics: ', get_data_descriptive_stats(data, TARGET_COLUMN))
    plot_hist(data, TARGET_COLUMN,jupyter=False)