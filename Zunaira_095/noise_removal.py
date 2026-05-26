import pandas as pd
import re

# 1. Load your structurally cleaned data
# (The one where we removed empty rows and filled blanks)
input_file = 'structurally_cleaned_data.xlsx'
df = pd.read_excel(input_file)

# The columns we want to clean
cols = [
    'What skills do you think you are lacking for a job?', 
    'If you could change one thing in your university system to better prepare students for jobs, what would it be?'
]

# 2. Define the Noise Removal function
def remove_noise(text):
    # Ensure the input is treated as a string
    text = str(text).lower()
    
    # Remove special characters and punctuation 
    # This keeps only lowercase letters (a-z) and spaces (\s)
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Remove extra whitespaces (e.g., "word   word" -> "word word")
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# 3. Apply the cleaning to your columns
for col in cols:
    df[col] = df[col].apply(remove_noise)

# 4. Save the result to a SEPARATE file
output_file = 'noise_removed_data.xlsx'
df.to_excel(output_file, index=False)

print(f"Noise removal complete! Data saved to: {output_file}")
print("Check the first few rows:")
print(df[cols].head())