import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
upTwo = "../../"
#upTwo = ""
df = pd.read_pickle(upTwo + "data/interim/data_processed.pkl")

print(df.info(verbose=True))

# Group similar columns based on your preference
ambient_columns = [
    'AmbientConditions.AmbientHumidity.U.Actual',
    'AmbientConditions.AmbientTemperature.U.Actual'
]

raw_material_columns = [
    'Machine1.RawMaterial.Property1',
    'Machine1.RawMaterial.Property2',
    # Add other similar columns here
]

machine1_columns = [
    'Machine1.RawMaterialFeederParameter.U.Actual',
    'Machine1.Zone1Temperature.C.Actual',
    # Add other machine 1 columns here
]

machine2_columns = [
    'Machine2.RawMaterialFeederParameter.U.Actual',
    'Machine2.Zone1Temperature.C.Actual',
    # Add other machine 2 columns here
]

# Create line plots for each group of columns
for group_name, columns in [("Ambient Conditions", ambient_columns),
                            ("Raw Material", raw_material_columns),
                            ("Machine 1", machine1_columns),
                            ("Machine 2", machine2_columns)]:
    plt.figure(figsize=(12, 6))
    for column in columns:
        plt.plot(df.index, df[column], label=column)
    plt.xlabel("Datetime")
    plt.ylabel("Value")
    plt.title(f"{group_name} Data")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()




# Define column groups using list comprehension
ambient_columns = [
    'AmbientConditions.AmbientHumidity.U.Actual',
    'AmbientConditions.AmbientTemperature.U.Actual'
]

raw_material_columns = [f'Machine{i}.RawMaterial.Property1' for i in range(1, 4)]
raw_material_columns.extend([f'Machine{i}.RawMaterial.Property2' for i in range(1, 4)])
raw_material_columns.extend([f'Machine{i}.RawMaterial.Property3' for i in range(1, 4)])

# Create line plots for each group of columns
column_groups = [ambient_columns, raw_material_columns]

for group in column_groups:
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    for column in group:
        sns.lineplot(x=df.index, y=df[column], label=column)
    plt.xlabel("Datetime")
    plt.ylabel("Value")
    plt.title(f"Line Plots for {', '.join(group)}")
    plt.legend(loc="best")
    plt.show()
