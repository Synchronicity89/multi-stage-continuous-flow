import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

upTwo = "../../"
#upTwo = ""
df = pd.read_pickle(upTwo + "data/interim/data_processed.pkl")


def clean_series(series, window_size=10, num_std_dev=3):
    """
    Clean a time series by removing extreme values and filling missing values
    using linear interpolation.
    Args:
    series (pd.Series): The input time series data. window_size (int): The window size for calculating moving averages and
    moving standard deviations.
    num_std_dev (int): The number of standard deviations to consider for identifying outliers.
    Returns:
    pd.Series: The cleaned time series data.

    """
    # Calculate the moving average and moving standard deviation
    moving_avg = series. rolling (window = window_size).mean()
    moving_std = series.rolling (window = window_size).std()
    # Identify outliers
    outliers = (np.abs (series - moving_avg) > num_std_dev * moving_std)
    # Replace outliers with NaN values
    cleaned_series = series.copy()
    cleaned_series [outliers] = np.nan
    # Fill missing values using linear interpolation
    cleaned_series. interpolate (method='linear', inplace=True)
    return cleaned_series
# Assuming your data is in a DataFrame named of
cleaned_series = clean_series (df ['Stage1.Output.Measurement0.U.Actual'])
cleaned_series.info(verbose=True)
cleaned_series.head(11)

df["Stage1.Output.Measurement0.U.Actual"] = cleaned_series

df = df.iloc[:, :42]

def engineer_features(df, lag_features, window_size=10):

    df_eng = df.copy()

    for col in lag_features:
        if col != 'Stage1.OUtput.Measurement0.U.Actual':
            for lag in range(1, window_size + 1):
                df_eng[f"{col}_lag{lag}"]  = df[col].shift(lag)

    for col in lag_features:
        if col != "Stage1.Output.Measurement0.U.Actual":
            df_eng[f"{col}_rolling_mean"] = df[col].rolling(window=window_size).mean()
            df_eng[f"{col}_rolling_std"] = df[col].rolling(window=window_size).std()
            df_eng[f"{col}_rolling_min"] = df[col].rolling(window=window_size).min()
            df_eng[f"{col}_rolling_max"] = df[col].rolling(window=window_size).max()

    df_eng = df_eng.dropna()

    return df_eng

lag_features = df.columns.tolist()
window_size = 10

df_eng = engineer_features(df, lag_features, window_size)
                  
df_eng.to_pickle(upTwo + "data/interim/data_engineered.pkl")
