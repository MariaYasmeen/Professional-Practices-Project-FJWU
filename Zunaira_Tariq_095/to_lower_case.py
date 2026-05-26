import pandas as pd

# 1. Load the .xlsx file
file_path = 'FJWU_Data_Fixed_Final.xlsx' 
df = pd.read_excel(file_path)

# 2. Define the columns to lower
cols_to_lower = [
    'What skills do you think you are lacking for a job?', 
    'If you could change one thing in your university system to better prepare students for jobs, what would it be?'
]

# 3. Convert only the specified columns to lowercase in the original DataFrame
for col in cols_to_lower:
    df[col] = df[col].astype(str).str.lower()

# 4. Save the entire DataFrame (with all columns) to the new file
df.to_excel('cleaned_data.xlsx', index=False)

print("Done! The .xlsx file has been processed and all columns were kept.")
