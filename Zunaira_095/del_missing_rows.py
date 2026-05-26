import pandas as pd

# Load the data
df = pd.read_excel('cleaned_data.xlsx')

cols = [
    'What skills do you think you are lacking for a job?', 
    'If you could change one thing in your university system to better prepare students for jobs, what would it be?'
]

# 1. This removes the rows in memory
df_clean = df.dropna(subset=cols, how='all').copy()

# 2. This fills empty cells in memory
df_clean[cols] = df_clean[cols].fillna("no response")

df = df.drop_duplicates().copy()

print(f"Duplicates removed. Rows remaining: {len(df)}")
# --- ADD THIS LINE TO SAVE IT TO YOUR COMPUTER ---
df_clean.to_excel('structurally_cleaned_data.xlsx', index=False)

print(f"Success! Saved {len(df_clean)} rows to 'structurally_cleaned_data.xlsx'")