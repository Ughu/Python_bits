import pandas as pd

# open the CSV file
df = pd.read_csv(r"file_path")

# split the dataframe into number of smaller dataframes with 30000 rows each.
# The numbers of dfs will depend on the number of rows on the original file.
dfs = [df[i:i+30000] for i in range(0, len(df), 30000)]

# save each smaller dataframe to a CSV file
for i, df_split in enumerate(dfs):
    df_split.to_csv(f'file_name{i}.csv', index=False)