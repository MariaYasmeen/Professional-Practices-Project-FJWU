import pandas as pd
import nltk
from nltk.corpus import stopwords
import ast

# Download the official list of English stopwords
nltk.download('stopwords')

# 1. Load the tokenized data
input_file = 'tokenized_data.xlsx'
df = pd.read_excel(input_file)

# Columns containing the tokens
# (Note: We use the '_tokens' columns we created in the last step)
token_cols = [
    'What skills do you think you are lacking for a job?_tokens', 
    'If you could change one thing in your university system to better prepare students for jobs, what would it be?_tokens'
]

# 2. Get the list of English stopwords
stop_words = set(stopwords.words('english'))

# Optional: Add custom stopwords that are common in your specific survey 
# but don't add value (like "university" or "student")
custom_stops = {'university', 'student', 'students', 'think', 'would', 'change', 'get'}
stop_words.update(custom_stops)

# 3. Stopword Removal Function
def remove_stopwords(token_list):
    # If Excel loaded the list as a string, convert it back to a Python list
    if isinstance(token_list, str):
        try:
            token_list = ast.literal_eval(token_list)
        except:
            return []
            
    # Keep the word ONLY if it's not in the stop_words set
    return [word for word in token_list if word not in stop_words]

# 4. Apply the removal
for col in token_cols:
    new_col_name = col.replace('_tokens', '_final_keywords')
    df[new_col_name] = df[col].apply(remove_stopwords)

# 5. Save the results
output_file = 'final_keywords_data.xlsx'
df.to_excel(output_file, index=False)

print(f"Stopword removal complete! Saved to: {output_file}")

# Show an example
print("\n--- Example ---")
print("Before:", df[token_cols[0]].iloc[0])
print("After :", df[token_cols[0].replace('_tokens', '_final_keywords')].iloc[0])