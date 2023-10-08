import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest, mutual_info_regression

# upTwo = "../../"
upTwo = ""

df = pd.read_pickle(upTwo + "data/interim/data_engineered.pkl")

def select_best_features(df: pd.DataFrame, target_column: str, k: int = 10) -> pd.DataFrame:
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    selector = SelectKBest(mutual_info_regression, k=k)

    selector.fit(X, y)

    top_features_indices = selector.get_support(indices=True)

    best_features = X.iloc[:, top_features_indices]

    return best_features

best_features_df = select_best_features(df, 'Stage1.Output.Measurement0.U.Actual')
print(best_features_df.columns)

best_features_df = pd.concat([best_features_df, df["Stage1.Output.Measurement0.U.Actual"]], axis= 1)

# moved this line after concat
best_features_df.to_pickle(upTwo + "data/processed/best_features.pkl")

# create a plot that provides an overview of best_features_df
import seaborn as sns

# sns.pairplot(best_features_df)
# plt.show()
# conda env update -n manufacturing-process --file environment.yml