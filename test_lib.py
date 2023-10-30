import pandas as pd
import matplotlib.pyplot as plt
from lib import load_data, get_data_descriptive_stats, plot_hist




def test_statistics():
    """Test function for column statistics"""
    data = pd.read_csv("src/Iris.csv")
    target_column = 'SepalLengthCm'

    res =  get_data_descriptive_stats(data, target_column)
    assert res['Mean'] == 5.843333333333334


  

def test_visualize_dataset():
    """Testing function for histogram of the target column"""

    data = load_data("src/Iris.csv")
    target_column = 'SepalLengthCm'


    # Test if the function executes without errors
    plot_hist(data, target_column,jupyter=False)

    # Capture the plot output and check if it's not empty
    fig = plt.gcf()
    assert len(fig.axes) > 0


if __name__ == '__main__':
    test_visualize_dataset()
    test_statistics()