import pandas as pd

# 1. Load the .xlsx file
file_path = 'structurally_cleaned_data.xlsx' 
df = pd.read_excel(file_path)

# 2. Define the columns we are working with
col_skills = 'What skills do you think you are lacking for a job?'
col_change = 'If you could change one thing in your university system to better prepare students for jobs, what would it be?'

# 3. Optional: Convert to lowercase first (from the previous step)
df[col_skills] = df[col_skills].astype(str).str.lower()
df[col_change] = df[col_change].astype(str).str.lower()

# 4. Create the new combined insights column
# We use a lambda function to cleanly connect the two answers into a full sentence
df['Combined_Insight'] = df.apply(
    lambda row: f"I lack {row[col_skills]} and I want the university to {row[col_change]}.", 
    axis=1
)

# 5. Save the entire DataFrame (including the new column)
df.to_excel('cleaned_data_with_insights.xlsx', index=False)

print("Done! The insights have been combined into a new column.")