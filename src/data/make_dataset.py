import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
print(os.getcwd())
#../../     is left out of path because os.getcwd() is root
# df = pd.read_csv("data/raw/continuous_factory_process.csv")
upTwo = "../../"
df = pd.read_csv(upTwo + "data/raw/continuous_factory_process.csv")

def preprocess_dataframe(df):
    """
    Preprocesses a given DataFrame:
    1. Selects the first 71 columns.
    2. Removes columns containing "SetPoint" in their names.
    3. Converst the "teim_stamp" column to a datetime object.
    4. Sets the "time_stamp" column as the index.

    Args:
        df (pd.DataFrame): The input DataFrame to be preprocessed.

        Returns:
        pd.DataFrame: The preprocessed DtatFrame.
    """

    selected_columns = df.columns[:71]
    df = df[selected_columns]

    # Get rid of columns that contain "Setpoint" in their name
    df = df.loc[:, ~df.columns.str.contains("Setpoint")]

    df["time_stamp"] = pd.to_datetime(df["time_stamp"])
    df = df.set_index("time_stamp")

    return df


processed_df = preprocess_dataframe(df)

processed_df.to_pickle(upTwo + "data/interim/data_processed.pkl")

