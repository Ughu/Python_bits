# Python_bits
This a repository with bits of python code to solve simple tasks.
The first one I am inserting here: Splitting CSV files into other csv files.

All code put in this repository must be commented and previously tested.
Ex:
```
import pandas as pd

# open the CSV file
df = pd.read_csv(r"file_path")

# split the dataframe into number of smaller dataframes with 30000 rows each.
# The numbers of dfs will depend on the number of rows on the original file.
dfs = [df[i:i+30000] for i in range(0, len(df), 30000)]

# save each smaller dataframe to a CSV file
for i, df_split in enumerate(dfs):
    df_split.to_csv(f'file_name{i}.csv', index=False)
```    
This is the first commit, an csv splitter into several csv files.
This repository should grow with time.
