import script
import pandas as pd



def test_descriptive_stats():
    "Test the descriptive stats function"
    data = pd.read_csv("src/Iris.csv")
    target_column = "SepalLengthCm"

    results = script.run_descriptive_stats(data, target_column)

    assert 'Mean' in results
    assert 'StdDev' in results
    assert 'Min' in results

