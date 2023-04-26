import pandas as pd

# open the CSV file
df = pd.read_csv(r"file_path")

# split the dataframe into number of smaller dataframes with 30000 rows each.
# The numbers of dfs will depend on the number of rows on the original file.
dfs = [df[i:i+30000] for i in range(0, len(df), 30000)]

# save each smaller dataframe to a CSV file
for i, df_split in enumerate(dfs):
    df_split.to_csv(f'file_name{i}.csv', index=False)


# Another option. This time we are splitting into 10 diferent files.
# Calculate the number of rows in each file
num_rows = len(df)
rows_per_file = num_rows // 10
remaining_rows = num_rows % 10

# Split the original file into 10 smaller files
for i in range(10):
    if i == 9:
        # Last file gets the remaining rows
        df_split = df[i * rows_per_file:i * rows_per_file + rows_per_file + remaining_rows]
    else:
        df_split = df[i * rows_per_file:i * rows_per_file + rows_per_file]
    
    # Write each split to a new CSV file
    df_split.to_csv(f'split_file_{i}.csv', index=False)
