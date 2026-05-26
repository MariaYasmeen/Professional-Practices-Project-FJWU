import pandas as pd
from collections import Counter
import ast

# 1. Load your fully cleaned data
input_file = 'fully_processed_data.xlsx'
df = pd.read_excel(input_file)

# The columns containing the lemmatized lists
cols = [
    'What skills do you think you are lacking for a job?_lemmatized', 
    'If you could change one thing in your university system to better prepare students for jobs, what would it be?_lemmatized'
]

# Function to count every word in a column
def get_full_frequency(df, col_name):
    all_keywords = []
    for row in df[col_name]:
        # Convert string representation of list back to real list
        if isinstance(row, str):
            try:
                words = ast.literal_eval(row)
                all_keywords.extend(words)
            except:
                continue
        elif isinstance(row, list):
            all_keywords.extend(row)
            
    # Count frequencies and sort from Highest to Lowest
    counts = Counter(all_keywords)
    freq_df = pd.DataFrame(counts.items(), columns=['Keyword', 'Frequency'])
    return freq_df.sort_values(by='Frequency', ascending=False)

# 2. Generate Frequency Dataframes
skills_freq = get_full_frequency(df, cols[0])
uni_change_freq = get_full_frequency(df, cols[1])

# 3. Save to one Excel file with two different sheets
output_file = 'Keyword_Frequency_Analysis.xlsx'
with pd.ExcelWriter(output_file) as writer:
    skills_freq.to_excel(writer, sheet_name='Lacking_Skills_Analysis', index=False)
    uni_change_freq.to_excel(writer, sheet_name='University_Changes_Analysis', index=False)

print(f"Analysis complete! Full frequencies saved to {output_file}")