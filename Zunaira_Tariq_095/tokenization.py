import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# --- UPDATE THESE LINES ---
nltk.download('punkt')
nltk.download('punkt_tab') # Add this line to fix the LookupError
# --------------------------

# ... the rest of your code stays the same ...
# 1. Load your noise-removed data
input_file = 'noise_removed_data.xlsx'
df = pd.read_excel(input_file)

# The columns we are analyzing
cols = [
    'What skills do you think you are lacking for a job?', 
    'If you could change one thing in your university system to better prepare students for jobs, what would it be?'
]

# 2. Tokenization Function
def tokenize_text(text):
    # Ensure text is a string; if it was "no response", it handles it correctly
    text = str(text)
    # This splits the sentence into a list of words
    return word_tokenize(text)

# 3. Apply tokenization to create NEW columns
# (We keep the old ones so you can compare)
for col in cols:
    new_col_name = col + '_tokens'
    df[new_col_name] = df[col].apply(tokenize_text)

# 4. Save to a new file
output_file = 'tokenized_data.xlsx'
df.to_excel(output_file, index=False)

print(f"Tokenization complete! Saved to: {output_file}")

# Let's see what happened to the first row
print("\n--- Example of Tokenization ---")
print("Before:", df[cols[0]].iloc[0])
print("After :", df[cols[0] + '_tokens'].iloc[0])